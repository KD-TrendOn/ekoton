import asyncio
import uvicorn
from app.main import app
from app.core.logger import setup_logger

logger = setup_logger(__name__)


async def main():
    logger.info("Initializing application")
    logger.info("Starting the API server")
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
