from uuid import UUID

from fastapi import APIRouter
from starlette.responses import UJSONResponse
from starlette.status import HTTP_201_CREATED

from database import queries
from schemas.orders import (
    OrderInput,
    OrderOutput,
)

orders_router = APIRouter()


@orders_router.post(
    "/orders",
    status_code=HTTP_201_CREATED,
    response_model=OrderInput,
    response_class=UJSONResponse,
)
async def post(order: OrderInput):
    return {}


@orders_router.get(
    "/orders/{order_id}",
    response_model=OrderOutput,
    response_class=UJSONResponse,
)
async def get(order_id: UUID):
    order = queries.get_order(order_id)
    return {
        "id": weather_forecast["id"],
        "status": weather_forecast["status"],
        "result": ujson.loads(weather_forecast["result"]) if weather_forecast["result"] else None,
    }
