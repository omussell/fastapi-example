from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///db.sqlite"

    class Config:
        env_file = ".env"

settings = Settings()
