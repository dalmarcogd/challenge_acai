from celery import Celery
from fastapi import FastAPI

from weather_forecast import __version__
from weather_forecast.database import migration
from weather_forecast.handlers.weather_forecast import weather_forecast_router
from weather_forecast.settings import CELERY, BASE_PATH, APPLICATION
from weather_forecast.tasks import task_registry

app = FastAPI(
    title="Weather Forecast API",
    version=__version__,
    docs_url=f"{BASE_PATH}/docs",
    redoc_url=f"{BASE_PATH}/redoc",
    openapi_url=f"{BASE_PATH}/openapi.json",
)

app.include_router(weather_forecast_router, prefix=f"{BASE_PATH}/v1")

app_celery = Celery(APPLICATION, tasks=task_registry, config_source=CELERY)
