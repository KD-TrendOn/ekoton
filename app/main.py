from fastapi import FastAPI
from app.api.v1.endpoints import submission, tasks, reports

app = FastAPI()

app.include_router(submission.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(reports.router, prefix="/api/v1")