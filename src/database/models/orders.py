from enum import Enum, IntEnum
from typing import Dict

from sqlalchemy import Column, Enum as EnumSqlAlchemy, Time, DECIMAL

from database.models.base import BaseModel


class OrderStage(str, Enum):
    choice = "choice"
    personalization = "personalization"
    done = "done"


class OrderSize(IntEnum):
    small = 1
    medium = 2
    big = 3


class OrderFlavor(IntEnum):
    strawberry = 1
    banana = 2
    kiwi = 3


class OrderPersonalization(IntEnum):
    granola = 1
    peanut_candy = 2
    ninho_milk = 3


class Order(BaseModel):
    __tablename__ = "orders"

    stage = Column(
        EnumSqlAlchemy(OrderStage), nullable=False, default=OrderStage.choice,
    )
    size = Column(EnumSqlAlchemy(OrderSize), nullable=False,)
    flavor = Column(EnumSqlAlchemy(OrderFlavor), nullable=False,)
    personalization = Column(EnumSqlAlchemy(OrderPersonalization), nullable=True,)
    setup_time = Column(Time, nullable=False)
    amount = Column(DECIMAL, nullable=False)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "stage": self.stage,
            "size": self.size,
            "flavor": self.flavor,
            "personalization": self.personalization,
            "setup_time": self.setup_time,
            "amount": self.amount,
        }
