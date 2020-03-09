from fastapi import FastAPI, Request
from starlette.responses import UJSONResponse

from exceptions.orders import OrderNotFoundException
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


@app.exception_handler(OrderNotFoundException)
def handle_order_not_found_exception(request: Request, exc: OrderNotFoundException):
    return UJSONResponse(status_code=400, content={"message": "Order Id not found."},)
