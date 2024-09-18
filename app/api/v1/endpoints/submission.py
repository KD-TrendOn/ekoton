from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import Any
import base64
from app.schemas.submission import SubmissionCreate, SubmissionResponse
from app.ml.classifier import classify_image
from db.crud import save_submission
from db.models import Submission
from db.db_helper import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/", response_model=SubmissionResponse)
async def create_submission(
    image: UploadFile = File(...),
    latitude: float = 0.0,
    longitude: float = 0.0,
    session: AsyncSession = Depends(db_helper.get_session),
):
    # Получение изображения
    content = await image.read()
    encoded_image = base64.b64encode(content).decode('utf-8')

    # Классификация изображения
    object_class = classify_image(content)

    # Создание объекта Submission
    submission = Submission(
        image=encoded_image,
        latitude=latitude,
        longitude=longitude,
        object_class=object_class,
    )

    # Сохранение в базу данных
    await save_submission(session, submission)

    return SubmissionResponse(
        id=submission.id,
        object_class=submission.object_class,
        latitude=submission.latitude,
        longitude=submission.longitude,
        created_at=submission.created_at,
    )