from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING, List
from sqlalchemy import (
    Boolean,
    Numeric,
    BigInteger,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.mdr import Mdr
from .cbs_type import Cbs_type
from .main_project import Main_project
from .base import Base

if TYPE_CHECKING:
    from models.mdr import Mdr


class Cbs_element(Base):
    __tablename__ = "cbs_element"
    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, index=True, autoincrement=True
    )
    old_id: Mapped[int | None]
    title: Mapped[str] = mapped_column(String(100))
    parent_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("cbs_element.id", ondelete="RESTRICT"),
        index=True,
        nullable=True,
    )
    main_project_id: Mapped[int] = mapped_column(
        ForeignKey("main_project.id"), index=True
    )
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    valid_to: Mapped[date] = mapped_column(nullable=True)
    valid_from: Mapped[date] = mapped_column(nullable=True)
    code: Mapped[str] = mapped_column(String(30))
    wbs_code: Mapped[str | None] = mapped_column(String(30), nullable=True)
    element_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("cbs_type.id"), index=True
    )
    rev_no: Mapped[int]
    is_valid: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)
    parent = relationship("Cbs_element", remote_side=[id], backref="children")
    cbs_type: Mapped[Cbs_type] = relationship(back_populates="cbs_element")
    main_project: Mapped[Main_project] = relationship(back_populates="cbs_element")
    contract_item: Mapped[List["Contract_item"]] = relationship(
        back_populates="cbs_element"
    )
    mdr: Mapped[List["Mdr"]] = relationship(back_populates="cbs_element")

    cbs_element_history: Mapped[List["Cbs_element_history"]] = relationship(
        back_populates="cbs_element"
    )
