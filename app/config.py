# 3rd-party
from pydantic import BaseSettings


class Settings(BaseSettings):
    version: str = "0.0.1"
    database_url: str = "sqlite:///db.sqlite"

    class Config:
        env_file = ".env"


settings = Settings()
