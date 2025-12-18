import datetime
from decimal import Decimal
from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .cbs_element import Cbs_element
from .base import Base


class Cbs_element_history(Base):
    __tablename__ = "cbs_element_history"
    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, index=True, autoincrement=True
    )
    cbs_element_id: Mapped[int] = mapped_column(
        ForeignKey("cbs_element.id"), index=True
    )
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    rev_no: Mapped[int]
    revision_date: Mapped[datetime.date]
    cbs_element: Mapped[Cbs_element] = relationship(
        back_populates="cbs_element_history"
    )
