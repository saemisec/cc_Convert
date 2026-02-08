from typing import TYPE_CHECKING, List
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .contract import Contract


class Delivery_type(Base):
    __tablename__ = "delivery_type"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(30), unique=True)
    contracts: Mapped[List["Contract"]] = relationship(back_populates="delivery_type")
