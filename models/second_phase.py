from typing import List
from .base import Base
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Second_Phase(Base):
    __tablename__ = "second_phase"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(10), unique=True)
    pre_contract: Mapped[List["Pre_contract"]] = relationship(
        back_populates="second_phase"
    )
    
    __table_args__ = (UniqueConstraint("name", name="uq_second_phase_name"),)
