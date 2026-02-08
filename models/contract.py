import datetime
from decimal import Decimal
import enum
from sqlalchemy import Date, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Contract_rate(enum.Enum):
    CONST_RATE = "نرخ ثابت"
    ATTACH_RATE = "نرخ ضمیمه"


class Contract(Base):
    __tablename__ = "contract"
    id: Mapped[int] = mapped_column(
        ForeignKey("pre_contract.id"), primary_key=True, index=True
    )
    insu_percent: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    tax_percent: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    is_vat_contain: Mapped[bool]
    delivery_type_id: Mapped[int | None] = mapped_column(ForeignKey("delivery_type.id"))
    prepayment_percent: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    delivery_type_desc: Mapped[str | None] = mapped_column(String(200))
    fine_percent: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    bank_account_id: Mapped[int] = mapped_column(ForeignKey("bank_account.id"))
    start_date: Mapped[datetime.date]
    end_date: Mapped[datetime.date | None]
    registration_date: Mapped[datetime.date] = mapped_column(
        Date, default=datetime.date.today
    )
    duration: Mapped[int]
    good_job_percent: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    prepayment_irr: Mapped[Decimal | None] = mapped_column(Numeric(18, 2))
    prepayment_cur: Mapped[Decimal | None] = mapped_column(Numeric(18, 2))
    contractor_obligations: Mapped[str | None] = mapped_column(String(500))
    employer_obligations: Mapped[str | None] = mapped_column(String(500))
    desc: Mapped[str | None] = mapped_column(String(500))
    contract_rate: Mapped[Contract_rate]
    cbs_assign: Mapped[bool] = mapped_column(default=False, nullable=True)
    pre_contract: Mapped["Pre_contract"] = relationship(back_populates="contract")
    bank_account: Mapped["Bank_Account"] = relationship(back_populates="contract")
    delivery_type: Mapped["Delivery_type"] = relationship(back_populates="contract")
