from typing import Dict, Union
from uuid import UUID

from sqlalchemy.orm import Query

import utils
from database.models import Flavor, Size, Customization
from database.models.orders import Order, OrderCustomization
from database.utils import db_session
from exceptions.orders import (
    OrderNotFoundException,
    SizeNotFoundException,
    FlavorNotFoundException,
    CustomizationNotFoundException,
)


def create_order(order: Dict) -> Dict:
    with db_session() as session:
        size = get_size_by_code(order.pop("size").value)
        if not size:
            raise SizeNotFoundException()
        flavor = get_flavor_by_code(order.pop("flavor").value)
        if not flavor:
            raise FlavorNotFoundException()

        new_order = Order(**order, size_id=size["id"], flavor_id=flavor["id"])

        new_order.setup_time = utils.calculate_time(size, flavor)
        new_order.amount = utils.calculate_amount(size)
        session.add(new_order)
        session.commit()
        return new_order.to_dict()


def update_order(order_id: UUID, order: Dict) -> Dict:
    with db_session() as session:
        order_update = Query(Order, session=session).filter_by(id=order_id).first()
        if not order_update:
            raise OrderNotFoundException()
        order_update_dict = order_update.to_dict()
        delete_customizations_by_order_id(order_id)

        customizations = []
        for customization_code in order["customizations"]:
            customization = get_customization_by_code(customization_code.value)
            customizations.append(customization)
            if not customization:
                raise CustomizationNotFoundException()

            session.add(
                OrderCustomization(
                    order_id=order_id, customization_id=customization["id"]
                )
            )
        size = get_size_by_id(order_update_dict["size_id"])
        flavor = get_flavor_by_id(order_update_dict["flavor_id"])
        order_update = Query(Order, session=session).filter_by(id=order_id).first()
        order_update.setup_time = utils.calculate_time(size, flavor, customizations)
        order_update.amount = utils.calculate_amount(size, customizations)
        session.commit()

    return get_order(order_id)


def get_order(order_id: UUID) -> Dict:
    with db_session() as session:
        order: Order = Query(Order, session=session).filter_by(id=order_id).one()
        return order.to_dict()


def get_flavor_by_code(flavor_code: int) -> Union[Dict, None]:
    with db_session() as session:
        flavor: Flavor = Query(Flavor, session=session).filter_by(
            code=flavor_code
        ).one()
        if not flavor:
            return None
        return flavor.to_dict()


def get_flavor_by_id(flavor_id: UUID) -> Union[Dict, None]:
    with db_session() as session:
        flavor: Flavor = Query(Flavor, session=session).filter_by(id=flavor_id).one()
        if not flavor:
            return None
        return flavor.to_dict()


def get_size_by_code(size_code: int) -> Union[Dict, None]:
    with db_session() as session:
        size: Size = Query(Size, session=session).filter_by(code=size_code).one()
        if not size:
            return None
        return size.to_dict()


def get_size_by_id(size_id: UUID) -> Union[Dict, None]:
    with db_session() as session:
        size: Size = Query(Size, session=session).filter_by(id=size_id).one()
        if not size:
            return None
        return size.to_dict()


def get_customization_by_code(customization_code: int) -> Union[Dict, None]:
    with db_session() as session:
        customization: Customization = Query(Customization, session=session).filter_by(
            code=customization_code
        ).one()
        if not customization:
            return None
        return customization.to_dict()


def get_customization_by_id(customization_id: UUID) -> Union[Dict, None]:
    with db_session() as session:
        customization: Customization = Query(Customization, session=session).filter_by(
            id=customization_id
        ).one()
        if not customization:
            return None
        return customization.to_dict()


def delete_customizations_by_order_id(order_id: UUID):
    with db_session() as session:
        Query(OrderCustomization, session=session).filter_by(order_id=order_id).delete()
