from typing import List
from .base import Base
from convert_models.bank import Bank
from convert_models.partner import Partner
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column

class Bank_Account(Base):
    __tablename__ = "bank_account"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    account_number : Mapped[str] = mapped_column(String(40))
    is_default : Mapped[bool]
    desc : Mapped[str | None] = mapped_column(String(200))
    bank_id : Mapped[int] = mapped_column(ForeignKey("bank.id"),index=True)
    parter_id : Mapped[int] = mapped_column(ForeignKey("partner.id"),index=True)
    bank : Mapped[Bank] = relationship(back_populates="bank_account")
    partner : Mapped[Partner] = relationship(back_populates="bank_account")
    contract : Mapped[List["Contract"]] = relationship(back_populates="bank_account")
