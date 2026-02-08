from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Department(Base):
    __tablename__ = "department"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(20), unique=True)
    # position: Mapped[List["Position"]] = relationship(back_populates="department")
