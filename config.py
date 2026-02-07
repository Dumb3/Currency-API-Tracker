from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_url: str
    database_url: str
    app_env: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
