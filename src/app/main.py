from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.infrastructure.config.database import init
from app.presentation.controllers.user_controller import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
