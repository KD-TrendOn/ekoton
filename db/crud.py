from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models.submission import Submission
from typing import Any

async def save_submission(session: AsyncSession, submission: Submission) -> None:
    session.add(submission)
    await session.commit()
    await session.refresh(submission)