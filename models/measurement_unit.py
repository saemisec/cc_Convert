from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Measurement_unit(Base):
    __tablename__ = "measurement_unit"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(30), unique=True)
    code: Mapped[str] = mapped_column(String(10), unique=True)
    is_nemeric: Mapped[bool]

    good: Mapped[List["Good"]] = relationship(back_populates="measurement_unit")
