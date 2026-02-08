from typing import TYPE_CHECKING, List
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .bank import Bank
from .partner import Partner
from .base import Base

if TYPE_CHECKING:
    from .contract import Contract


class Bank_Account(Base):
    __tablename__ = "bank_account"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    account_number: Mapped[str] = mapped_column(String(40))
    is_default: Mapped[bool]
    desc: Mapped[str | None] = mapped_column(String(200))
    bank_id: Mapped[int] = mapped_column(ForeignKey("bank.id"), index=True)
    partner_id: Mapped[int] = mapped_column(ForeignKey("partner.id"), index=True)
    bank: Mapped[Bank] = relationship(back_populates="bank_account")
    partner: Mapped[Partner] = relationship(back_populates="bank_account")
    contracts: Mapped[List["Contract"]] = relationship(back_populates="bank_account")

    __table_args__ = (
        UniqueConstraint(
            "bank_id", "partner_id", "account_number", name="uq_bank_account_composite"
        ),
    )
