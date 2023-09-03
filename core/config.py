from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    # echo: bool = False
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()

    # db_echo: bool = True


settings = Settings()
