from typing import List
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Main_phase(Base):
    __tablename__ = "main_phase"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    contracts: Mapped[List["Contract"]] = relationship(back_populates="main_phase")
