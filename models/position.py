from typing import List
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.department import Department
from .base import Base


class Position(Base):
    __tablename__ = "position"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"), index=True)
    user_position: Mapped[List["User_position"]] = relationship(
        back_populates="position"
    )
    department: Mapped[Department] = relationship(back_populates="position")

    __table_args__ = (UniqueConstraint("name", name="uq_position_name"),)
