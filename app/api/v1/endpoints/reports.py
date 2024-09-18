# app/api/v1/endpoints/reports.py
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.reports import ReportResponse
from db.crud import get_submissions_within_park
from db.db_helper import db_helper

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)

@router.get("/park", response_model=List[ReportResponse])
async def get_park_report(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    submissions = await get_submissions_within_park(session)
    return [ReportResponse.from_orm(sub) for sub in submissions]
