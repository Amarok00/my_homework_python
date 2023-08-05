from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# DB_FILE = BASE_DIR / "app.db"
DEFAULT_DB_URL = "postgresql://username:passwd@0.0.0.0:5434/blog"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DEFAULT_DB_URL,
)

class Config:
    TESTING = False
    DEBUG = False
    SECRET_KEY = "8479a708f45e33c45978f61936f4b70b"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

class ProductionConfig(Config):
    SECRET_KEY = "32e9901c4121506093e683ec5860df30"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True