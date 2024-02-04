from decimal import Decimal
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import (
    BaseModelCreatedUpdated,
    BaseModelUUID,
)


class Product(BaseModelUUID, BaseModelCreatedUpdated):
    __tablename__ = "product"

    title: Mapped[str] = mapped_column(String(255))
    cost: Mapped[Decimal] = mapped_column()
