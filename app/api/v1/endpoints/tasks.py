# app/api/v1/endpoints/tasks.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.tasks import TaskCreate, TaskResponse
from db.crud import create_task, get_active_tasks
from db.models import Task
from db.db_helper import db_helper

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post("/", response_model=TaskResponse)
async def create_new_task(
    task: TaskCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    new_task = Task(**task.dict())
    created_task = await create_task(session, new_task)
    return TaskResponse.from_orm(created_task)

@router.get("/", response_model=List[TaskResponse])
async def get_tasks(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    tasks = await get_active_tasks(session)
    print(tasks[0])
    answer = []
    for task in tasks:
        ans = task.__dict__
        ans["status"] = 255
        answer.append(TaskResponse(**ans))
    return answer
