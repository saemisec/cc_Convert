from typing import List
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Currency(Base):
    __tablename__ = "currency"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(20), unique=True)
    contracts: Mapped[List["Contract"]] = relationship(
        back_populates="currency", lazy="selectin"
    )
    main_project: Mapped[List["Main_project"]] = relationship(
        back_populates="currency", lazy="selectin"
    )
