from typing import TYPE_CHECKING, List
from sqlalchemy import Identity, String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .permission import Permission


class Form_Entity(Base):
    __tablename__ = "form_entity"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))
    permission: Mapped[List["Permission"]] = relationship(back_populates="form_entity")

    __table_args__ = (UniqueConstraint("name", name="uq_form_entity_name"),)
