from datetime import time
from decimal import Decimal
from enum import Enum
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel

from database.models.orders import OrderStage


class OrderFlavor(int, Enum):
    strawberry = 1
    banana = 2
    kiwi = 3


class OrderSize(int, Enum):
    small = 1
    medium = 2
    big = 3


class OrderCustomization(int, Enum):
    granola = 1
    peanut_candy = 2
    ninho_milk = 3


class OrderInput(BaseModel):
    size: OrderSize
    flavor: OrderFlavor


class OrderOutput(BaseModel):
    id: UUID
    size: OrderSize
    flavor: OrderFlavor
    customizations: Optional[List[OrderCustomization]]
    stage: OrderStage
    setup_time: time
    amount: Decimal


class OrderCustomizationInput(BaseModel):
    customizations: List[OrderCustomization]
