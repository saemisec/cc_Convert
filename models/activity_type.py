from typing import TYPE_CHECKING, List
from sqlalchemy import Identity, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .permission import Permission


class Activity_type(Base):
    __tablename__ = "activity"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, index=True)

    permission: Mapped[List["Permission"]] = relationship(
        back_populates="activity_type"
    )
