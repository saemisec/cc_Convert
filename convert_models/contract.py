import datetime
from typing import List
from .base import Base
import enum
from sqlalchemy import String, ForeignKey,BigInteger
from sqlalchemy.orm import relationship,Mapped, mapped_column, mapped_column


class Contract_rate(enum.Enum):
        CONST_RATE = "نرخ ثابت"
        ATTACH_RATE = "نرخ ضمیمه"

class Contract(Base):
    __tablename__ = "contract"
    id : Mapped[int] = mapped_column(ForeignKey("pre_contract.id"),primary_key=True,index=True)
    insu_percent : Mapped[float]
    tax_percent : Mapped[float]
    is_vat_contain : Mapped[bool]
    delivery_type_id : Mapped[int | None] = mapped_column(ForeignKey("delivery_type.id"))
    prepayment_percent : Mapped[float | None]
    delivery_type_desc : Mapped[str | None] = mapped_column(String(200))
    fine_percent : Mapped[float | None]
    bank_account_id : Mapped[int] = mapped_column(ForeignKey("bank_account.id"))
    start_date : Mapped[datetime.date]
    registration_date : Mapped[datetime.date]
    duration : Mapped[int]
    good_job_percent : Mapped[float | None]
    prepayment_irr : Mapped[int| None] = mapped_column(BigInteger)
    prepayment_cur : Mapped[int| None] = mapped_column(BigInteger)
    contractor_obligations : Mapped[str | None] = mapped_column(String(500))
    employer_obligations : Mapped[str | None] = mapped_column(String(500))
    desc : Mapped[str | None] = mapped_column(String(500))
    contract_rate : Mapped[Contract_rate]

    pre_contract : Mapped["Pre_contract"] = relationship(back_populates="contract")
    bank_account : Mapped["Bank_Account"] = relationship(back_populates="contract")
    delivery_type : Mapped["Delivery_type"] = relationship(back_populates="contract")
    payment_condition : Mapped[List["Payment_condition"]] = relationship(back_populates="contract")