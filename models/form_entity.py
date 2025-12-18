from typing import List
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Form_Entity(Base):
    __tablename__ = "form_entity"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    permission: Mapped[List["Permission"]] = relationship(back_populates="form_entity")

    __table_args__ = (UniqueConstraint("name", name="uq_form_entity_name"),)
