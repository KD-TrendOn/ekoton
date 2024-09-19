from fastapi import FastAPI
from app.api.v1.endpoints import submission, tasks, reports
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

class DynamicCORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS":
            response = await call_next(request)
        else:
            origin = request.headers.get("origin")
            response = await call_next(request)
            response.headers["Access-Control-Allow-Origin"] = origin
        return response



app = FastAPI()
app.add_middleware(DynamicCORSMiddleware)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Received request: {request.method} {request.url}")
    print(f"Headers: {request.headers}")
    response = await call_next(request)
    print(f"Response status: {response.status_code}")
    return response

app.include_router(submission.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(reports.router, prefix="/api/v1")