from enum import Enum
from typing import Dict

from sqlalchemy import Column, JSON, Enum as EnumSqlAlchemy

from database.models.base import BaseModel


class OrderStage(str, Enum):
    choice = "choice"
    personalization = "personalization"
    done = "done"


class Order(BaseModel):
    __tablename__ = "orders"

    stage = Column(
        EnumSqlAlchemy(OrderStage),
        nullable=False,
        default=OrderStage.choice,
    )
    params = Column(JSON, nullable=False)
    result = Column(JSON, nullable=True)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "status": self.status,
            "result": self.result,
        }
