from typing import List
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Cbs_type(Base):
    __tablename__ = "cbs_type"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    cbs_element: Mapped[List["Cbs_element"]] = relationship(back_populates="cbs_type")
