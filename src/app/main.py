from fastapi import FastAPI

from app.infrastructure.config.settings import settings
from app.presentation.controllers.auth_controller import router as auth_router
from app.presentation.controllers.user_controller import router as user_router

app = FastAPI(
    title='FastAPI Clean Architecture',
)

app.include_router(
    user_router, prefix=f'{settings.API_PREFIX}/users', tags=['users']
)
app.include_router(
    auth_router, prefix=f'{settings.API_PREFIX}/auth', tags=['auth']
)
