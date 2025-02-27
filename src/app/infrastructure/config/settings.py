from pydantic_settings import BaseSettings, SettingsConfigDict

from app.constants import Environment


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='allow',
    )

    ENVIRONMENT: Environment = Environment.LOCAL
    DATABASE_URL: str
    API_PREFIX: str = '/v1'
    JWT_SECRET: str
    JWT_EXPIRATION: int = 60
    JWT_ALGORITHM: str = 'HS512'


settings: Settings = Settings()
