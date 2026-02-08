from typing import TYPE_CHECKING, List
from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

if TYPE_CHECKING:
    from .contract import Contract


class Second_Phase(Base):
    __tablename__ = "second_phase"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(10), unique=True)
    contracts: Mapped[List["Contract"]] = relationship(back_populates="second_phase")
    # purchase_requests: Mapped[List["Purchase_request"]] = relationship(
    #     back_populates="second_phase"
    # )
