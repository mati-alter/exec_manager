from contextlib import asynccontextmanager

from core.logging import setup_logging
from fastapi import FastAPI

logger = setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("App started")
    yield
    logger.info("App stopped")


app = FastAPI(title="Exec Manager", lifespan=lifespan)


@app.get("/")
async def health() -> dict[str, str]:
    return {"status": "ok"}
