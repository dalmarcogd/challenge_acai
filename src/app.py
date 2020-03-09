from fastapi import FastAPI

from handlers.orders import orders_router
from settings import BASE_PATH
from src import __version__

app = FastAPI(
    title="Acai API",
    version=__version__,
    docs_url=f"{BASE_PATH}/docs",
    redoc_url=f"{BASE_PATH}/redoc",
    openapi_url=f"{BASE_PATH}/openapi.json",
)

app.include_router(orders_router, prefix=f"{BASE_PATH}/v1")
