import datetime
from decimal import Decimal
from sqlalchemy import Numeric, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base
from .contract_item import Contract_item


class Contract_item_history(Base):
    __tablename__ = "contract_item_history"
    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, index=True, autoincrement=True
    )
    contract_item_id: Mapped[int] = mapped_column(
        ForeignKey("contract_item.id"), index=True
    )
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    register_date: Mapped[datetime.date]
    contract_item: Mapped[Contract_item] = relationship(
        back_populates="contract_item_history"
    )
