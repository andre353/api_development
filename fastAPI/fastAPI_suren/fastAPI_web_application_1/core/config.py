from pathlib import Path
from os import getenv
from pydantic_settings import BaseSettings

# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    # db_echo: bool = False
    db_echo: bool = True


# создаем экземпляр, который будем дальше использовать внутри проекта
# после будем использовать settings.db_url, чтобы подключаться к нашей базе данных именно по этому адресу
settings = Setting()
