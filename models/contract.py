import datetime
from decimal import Decimal
import enum
from typing import TYPE_CHECKING, List
from sqlalchemy import Date, Numeric, String, ForeignKey, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .main_phase import Main_phase
    from .second_phase import Second_Phase
    from .main_project import Main_project
    from .partner import Partner
    from .currency import Currency
    from .bank_account import Bank_Account
    from .delivery_type import Delivery_type
    from .demand_document import Demand_document
    from .payment_condition import Payment_Condition
    from .contract_item import Contract_Item


# class Contract_rate(enum.Enum):
#     CONST_RATE = "نرخ ثابت"
#     ATTACH_RATE = "نرخ ضمیمه"


class Contract_status(enum.Enum):
    INPROGRESS = "InProgress"
    CANCELED = "Canceled"
    FINISHED = "Finished"


class Contract(Base):
    """Contract model - merged from Pre_contract and Contract"""

    __tablename__ = "contract"

    # Primary key
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)

    # Fields from Pre_contract
    old_id: Mapped[int | None]
    title: Mapped[str] = mapped_column(String(200))
    partner_id: Mapped[int] = mapped_column(ForeignKey("partner.id"), index=True)
    main_project_id: Mapped[int] = mapped_column(
        ForeignKey("main_project.id"), index=True
    )
    number: Mapped[str] = mapped_column(String(50))
    request_number: Mapped[str] = mapped_column(String(30))
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    register_date: Mapped[datetime.date] = mapped_column(
        Date, default=datetime.date.today
    )
    # register_duration: Mapped[int]
    contract_status: Mapped[Contract_status]
    currency_id: Mapped[int | None] = mapped_column(
        ForeignKey("currency.id"), index=True
    )
    main_phase_id: Mapped[int | None] = mapped_column(
        ForeignKey("main_phase.id"), index=True
    )
    second_phase_id: Mapped[int | None] = mapped_column(
        ForeignKey("second_phase.id"), index=True
    )

    # Reference to source demand_document (contract request)
    demand_document_id: Mapped[int | None] = mapped_column(
        ForeignKey("demand_document.id"), index=True, nullable=True
    )

    # Fields from original Contract model
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
    # contract_rate: Mapped[Contract_rate]
    # cbs_assign: Mapped[bool] = mapped_column(default=False, nullable=True)

    # Relationships from Pre_contract
    main_project: Mapped["Main_project"] = relationship(back_populates="contracts")
    partner: Mapped["Partner"] = relationship(back_populates="contracts")
    currency: Mapped["Currency | None"] = relationship(back_populates="contracts")
    main_phase: Mapped["Main_phase | None"] = relationship(back_populates="contracts")
    second_phase: Mapped["Second_Phase | None"] = relationship(
        back_populates="contracts"
    )

    # Relationships from original Contract
    bank_account: Mapped["Bank_Account"] = relationship(back_populates="contracts")
    delivery_type: Mapped["Delivery_type | None"] = relationship(
        back_populates="contracts"
    )

    # Relationship to source demand_document
    demand_document: Mapped["Demand_document | None"] = relationship(
        back_populates="contracts"
    )

    # Relationship to payment conditions
    payment_conditions: Mapped[List["Payment_Condition"]] = relationship(
        back_populates="contract"
    )

    # Relationship to contract items
    contract_items: Mapped[List["Contract_Item"]] = relationship(
        back_populates="contract"
    )
