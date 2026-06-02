from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logging import setup_logging
from app.db.session import get_db

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


@app.get("/db-check")
async def db_check(db: AsyncSession = Depends(get_db)):
    return await db.execute(text("SELECT 1"))
