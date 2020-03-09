import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config("DEBUG", default=False, cast=bool)
AUTO_RELOAD = DEBUG
PORT = config("PORT", default=8000, cast=int)
HOST = config("HOST")
WORKERS = 2
BASE_PATH = config("BASE_PATH")
APPLICATION = config("APPLICATION")

DATABASE_URI = (
    f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@"
    f"{config('DB_HOST')}/{config('DB_NAME')}"
)
