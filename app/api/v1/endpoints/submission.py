from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
import base64
from app.schemas.submissions import SubmissionCreate, SubmissionResponse
from db.crud import create_submission
from db.models import Submission
from db.db_helper import db_helper
from app.ml.classifier import classify_image

router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"],
)

@router.post("/", response_model=SubmissionResponse)
async def create_user_submission(
    submission: SubmissionCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    # Декодирование изображения из base64
    try:
        image_data = base64.b64decode(submission.image)
    except:
        raise HTTPException(status_code=400, detail="Invalid image encoding")

    # Классификация изображения
    object_class = classify_image(image_data)

    # Создание объекта Submission
    new_submission = Submission(
        image=submission.image,
        latitude=submission.latitude,
        longitude=submission.longitude,
        object_class=object_class,
    )

    # Сохранение в базу данных
    created_submission = await create_submission(session, new_submission)

    return SubmissionResponse(
        id=created_submission.id,
        object_class=created_submission.object_class,
        latitude=created_submission.latitude,
        longitude=created_submission.longitude,
        status=created_submission.status,
        created_at=created_submission.created_at,
    )
