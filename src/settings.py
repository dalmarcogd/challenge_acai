import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_PATH = config("BASE_PATH")

DATABASE_URI = (
    f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@"
    f"{config('DB_HOST')}/{config('DB_NAME')}"
)
