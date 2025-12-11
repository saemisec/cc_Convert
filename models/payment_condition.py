import datetime
from .base import Base
from sqlalchemy import String, ForeignKey,BigInteger
from sqlalchemy.orm import relationship,Mapped, mapped_column, mapped_column
from models.contract import Contract

class Payment_condition(Base):
    __tablename__ = "payment_condition"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    desc : Mapped[str ] = mapped_column(String(300))
    value : Mapped[int ]
    contract_id : Mapped[int | None] = mapped_column(ForeignKey("contract.id"),index=True)
    contract : Mapped[Contract] = relationship(back_populates="payment_condition")
