from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', case_sensitive=True, extra="allow"
    )

    DATABASE_URL: str
    API_PREFIX: str = "/v1"


settings: Settings = Settings()
