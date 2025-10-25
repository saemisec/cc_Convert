from .base import Base
from sqlalchemy import String
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship



class Department(Base):
    __tablename__ = "department"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    name : Mapped[str] = mapped_column(String(20),unique=True)
    user: Mapped[List["User"]] = relationship(back_populates="department")