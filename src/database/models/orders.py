from enum import Enum
from typing import Dict

from sqlalchemy import (
    Column,
    Enum as EnumSqlAlchemy,
    Time,
    DECIMAL,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.models.base import BaseModel


class OrderStage(str, Enum):
    choice = "choice"
    customization = "customization"
    done = "done"


class Size(BaseModel):
    __tablename__ = "sizes"

    code = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)
    amount = Column(DECIMAL, nullable=False)
    setup_time = Column(Time, nullable=False)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "code": self.code,
            "name": self.name,
            "amount": self.amount,
            "setup_time": self.setup_time,
        }


class Flavor(BaseModel):
    __tablename__ = "flavors"

    code = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)
    setup_time = Column(Time, nullable=False)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "code": self.code,
            "name": self.name,
            "setup_time": self.setup_time,
        }


class Customization(BaseModel):
    __tablename__ = "customizations"

    code = Column(Integer, nullable=False, unique=True)
    name = Column(String, nullable=False)
    amount = Column(DECIMAL, nullable=False)
    setup_time = Column(Time, nullable=False)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "code": self.code,
            "name": self.name,
            "amount": self.amount,
            "setup_time": self.setup_time,
        }


class OrderCustomization(BaseModel):
    __tablename__ = "order_customization"

    order_id = Column(ForeignKey("orders.id"), primary_key=True)
    customization_id = Column(ForeignKey("customizations.id"), primary_key=True)
    order = relationship("Order", foreign_keys="OrderCustomization.order_id")
    customization = relationship(
        "Customization", foreign_keys="OrderCustomization.customization_id"
    )

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "order_id": self.order_id,
            "customization_id": self.customization_id,
        }


class Order(BaseModel):
    __tablename__ = "orders"

    stage = Column(
        EnumSqlAlchemy(OrderStage), nullable=False, default=OrderStage.choice,
    )
    size_id = Column(ForeignKey("sizes.id"), nullable=False)
    size = relationship("Size", foreign_keys="Order.size_id")
    flavor_id = Column(ForeignKey("flavors.id"), nullable=False)
    flavor = relationship("Flavor", foreign_keys="Order.flavor_id")
    customizations = relationship("OrderCustomization", back_populates="order")

    setup_time = Column(Time, nullable=False)
    amount = Column(DECIMAL, nullable=False)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "stage": self.stage,
            "size_id": self.size_id,
            "flavor_id": self.flavor_id,
            "customizations": [
                c.to_dict() for c in self.customizations if self.customizations
            ],
            "setup_time": self.setup_time,
            "amount": self.amount,
        }
