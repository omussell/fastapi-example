from pydantic import BaseSettings, PostgresDsn

class Settings(BaseSettings):
    test_key: str = "test"
    database_url: str = "sqlite:///home/oem/fastapi-example/db.sqlite3"
    #db_url: PostgresDsn = "postgres://user:pass@localhost:5432/foobar"
    
    class Config:
        env_file = ".env"

settings = Settings()
