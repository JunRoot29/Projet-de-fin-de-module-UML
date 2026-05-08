import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IS_VERCEL = os.environ.get("VERCEL") == "1"
DEFAULT_DB_PATH = Path("/tmp/app.db") if IS_VERCEL else BASE_DIR / "app.db"
DEFAULT_UPLOAD_FOLDER = Path("/tmp/uploads") if IS_VERCEL else BASE_DIR / "uploads"


def sqlite_uri(path):
    return f"sqlite:///{path.as_posix()}"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", sqlite_uri(DEFAULT_DB_PATH)
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", str(DEFAULT_UPLOAD_FOLDER))
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
