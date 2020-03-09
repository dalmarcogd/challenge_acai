from datetime import datetime, date, time, timedelta
from decimal import Decimal
from typing import List, Dict


def calculate_amount(size: Dict, customizations: List[Dict] = None) -> Decimal:
    if not customizations:
        customizations = []
    return Decimal(size["amount"] + sum([c["amount"] for c in customizations]))


def calculate_time(
    size: Dict, flavor: Dict, customizations: List[Dict] = None,
) -> time:
    setup_time = (
        datetime.combine(date.min, size["setup_time"])
        + timedelta(
            hours=flavor["setup_time"].hour,
            minutes=flavor["setup_time"].minute,
            seconds=flavor["setup_time"].second,
        )
    ).time()
    if customizations:
        for c in customizations:
            setup_time = (datetime.combine(date.min, setup_time) + timedelta(
                hours=c["setup_time"].hour,
                minutes=c["setup_time"].minute,
                seconds=c["setup_time"].second,
            )).time()
    return setup_time
