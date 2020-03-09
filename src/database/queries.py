from typing import Dict
from uuid import UUID

from sqlalchemy.orm import Query

from database.models.orders import Order
from database.utils import db_session


def create_order(order: Dict) -> Dict:
    with db_session() as session:
        new_order = Order(**order)
        session.add(new_order)
        session.commit()
        return new_order.to_dict()


def update_order(order_ir: UUID, order: Dict) -> Dict:
    with db_session() as session:
        updated_order: Order = Query(Order, session=session).filter_by(
            id=order_ir
        ).update(**order)
        return updated_order.to_dict()


def get_order(order_id: UUID) -> Dict:
    with db_session() as session:
        order: Order = Query(Order, session=session).filter_by(id=order_id).one()
        return order.to_dict()
