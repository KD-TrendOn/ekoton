# app/api/v1/endpoints/reports.py
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.reports import ParkReport
from db.crud import get_submissions_within_park
from db.db_helper import db_helper
from collections import Counter

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)

@router.get("/park", response_model=ParkReport)
async def get_park_report(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    submissions = await get_submissions_within_park(session)
    
    # Подсчет количества объектов каждого класса
    class_counts = Counter(sub.object_class for sub in submissions)
    
    # Создание словаря с количеством для каждого класса
    statistics = {class_name: class_counts.get(class_name, 0) for class_name in CLASSES}
    
    return ParkReport(statistics=statistics)
