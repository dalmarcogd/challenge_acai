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

CELERY = {
    "CELERY_BROKER_URL": config("CELERY_BROKER_URL"),
    "CELERY_RESULT_BACKEND": config("CELERY_RESULT_BACKEND"),
}

DATABASE_URI = (
    f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@"
    f"{config('DB_HOST')}/{config('DB_NAME')}"
)
