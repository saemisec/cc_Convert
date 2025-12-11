from typing import List
from .base import Base
from sqlalchemy import Column, Integer, String,UniqueConstraint
from sqlalchemy.orm import relationship,Mapped, mapped_column



class Main_phase(Base):
    __tablename__ = "main_phase"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30),unique=True)
    pre_contract: Mapped[List["Pre_contract"]] = relationship(back_populates="main_phase")
