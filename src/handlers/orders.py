from uuid import UUID

from fastapi import APIRouter
from starlette.responses import UJSONResponse
from starlette.status import HTTP_201_CREATED

from database import queries
from schemas.orders import OrderInput, OrderOutput, OrderCustomizationInput

orders_router = APIRouter()


@orders_router.post(
    "/orders",
    status_code=HTTP_201_CREATED,
    response_model=OrderOutput,
    response_class=UJSONResponse,
)
async def post(order: OrderInput):
    order_created = queries.create_order(order.dict())
    flavor = queries.get_flavor_by_id(order_created["flavor_id"])
    size = queries.get_size_by_id(order_created["size_id"])
    return {**order_created, "size": size["code"], "flavor": flavor["code"]}


@orders_router.get(
    "/orders/{order_id}", response_model=OrderOutput, response_class=UJSONResponse,
)
async def get(order_id: UUID):
    order = queries.get_order(order_id)
    flavor = queries.get_flavor_by_id(order["flavor_id"])
    size = queries.get_size_by_id(order["size_id"])
    return {**order, "size": size["code"], "flavor": flavor["code"]}


@orders_router.put(
    "/orders/{order_id}/customizations",
    response_model=OrderOutput,
    response_class=UJSONResponse,
)
async def put(order_id: UUID, order_customization: OrderCustomizationInput):
    order = queries.update_order(order_id, order_customization.dict())
    flavor = queries.get_flavor_by_id(order["flavor_id"])
    size = queries.get_size_by_id(order["size_id"])
    customizations = order.pop("customizations")
    customization_codes = []
    for customization in customizations:
        custom = queries.get_customization_by_id(customization["customization_id"])
        if custom:
            customization_codes.append(custom["code"])
    return {
        **order,
        "size": size["code"],
        "flavor": flavor["code"],
        "customizations": customization_codes,
    }
