from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.infrastructure.config.database import init
from app.infrastructure.config.settings import settings
from app.presentation.controllers.user_controller import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield


app = FastAPI(
    title='FastAPI Clean Architecture',
    lifespan=lifespan,
)

app.include_router(
    user_router, prefix=f'{settings.API_PREFIX}/users', tags=['users']
)
