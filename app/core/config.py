from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Exec Manager"
    DEBUG: bool = False
    DB_URL: str = ""
    DB_PASS: str = ""
    DB_PORT: int = 5432
    REDIS_HOST: str = ""
    REDIS_URL: str = ""
    REDIS_PORT: int = 6379
    REDIS_PASS: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
