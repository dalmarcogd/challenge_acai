import abc
from datetime import datetime
from typing import Dict
from uuid import uuid4

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

DeclarativeModel = declarative_base()


class BaseModel(DeclarativeModel):
    __abstract__ = True
    id = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        primary_key=True,
        index=True,
        default=uuid4,
    )
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, nullable=True, default=None, onupdate=datetime.utcnow()
    )

    @abc.abstractmethod
    def to_dict(self) -> Dict:
        raise NotImplementedError("Implement method `to_dict`, must be return a Dict.")
