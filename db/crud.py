# db/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Submission, Task
from typing import List
from app.core.constants import is_within_park

async def create_submission(session: AsyncSession, submission: Submission) -> Submission:
    session.add(submission)
    await session.commit()
    await session.refresh(submission)
    return submission

async def get_submissions(session: AsyncSession, skip: int = 0, limit: int = 10) -> List[Submission]:
    stmt = select(Submission).offset(skip).limit(limit)
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_submission_by_id(session: AsyncSession, submission_id: int) -> Submission:
    stmt = select(Submission).where(Submission.id == submission_id).options(selectinload(Submission.user))
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

# Добавь аналогичные функции для других моделей по необходимости

async def create_task(session: AsyncSession, task: Task) -> Task:
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task

async def get_active_tasks(session: AsyncSession) -> List[Task]:
    stmt = select(Task).where(Task.is_active == True)
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_submissions_within_park(session: AsyncSession) -> List[Submission]:
    stmt = select(Submission)
    result = await session.execute(stmt)
    submissions = result.scalars().all()
    return [sub for sub in submissions if is_within_park(sub.latitude, sub.longitude)]
