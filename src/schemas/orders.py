from datetime import time
from uuid import UUID

from pydantic import BaseModel

from database.models.orders import OrderSize, OrderFlavor


class OrderInput(BaseModel):
    size: OrderSize
    flavor: OrderFlavor


class OrderOutput(BaseModel):
    id: UUID
    size: OrderSize
    flavor: OrderFlavor
    setup_time: time
