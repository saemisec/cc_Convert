import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import Date, Identity, Numeric, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .pre_contract import Pre_contract


class Addendum(Base):
    __tablename__ = "addendum"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    old_id: Mapped[int | None]
    title: Mapped[str] = mapped_column(String(100))
    contract_id: Mapped[int] = mapped_column(ForeignKey("pre_contract.id"))
    rev_no: Mapped[int]
    revdate: Mapped[datetime.date]
    revdesc: Mapped[str | None] = mapped_column(String(100))
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    duration: Mapped[int | None]
    regdate: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)
    # precontract: Mapped["Pre_contract"] = relationship(back_populates="addendum")
