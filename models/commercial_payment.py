from typing import TYPE_CHECKING
from decimal import Decimal
from sqlalchemy import (
    Identity,
    String,
    Integer,
    Boolean,
    Text,
    Date,
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .contract import Contract
    from .main_project import Main_project


class CommercialPayment(Base):
    """Commercial payment request - درخواست پرداخت قراردادی واحد بازرگانی"""

    __tablename__ = "commercial_payment"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)

    # Header info
    project_id: Mapped[int] = mapped_column(ForeignKey("main_project.id"), index=True)
    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"), index=True)
    report_number: Mapped[str | None] = mapped_column(String(50), nullable=True)
    report_date: Mapped[str | None] = mapped_column(Date, nullable=True)
    payment_turn: Mapped[int | None] = mapped_column(Integer, nullable=True)
    invoice_date: Mapped[str | None] = mapped_column(Date, nullable=True)
    contractor_invoice: Mapped[str | None] = mapped_column(String(100), nullable=True)
    attachment: Mapped[str | None] = mapped_column(String(200), nullable=True)

    # Payment details
    requested_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=0)
    insurance_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )
    payment_type: Mapped[str | None] = mapped_column(String(30), nullable=True)
    contractor_penalty: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )
    other_deductions: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )
    payable_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )

    # Account & progress
    deposit_account_number: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )
    financial_progress_percent: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 2), nullable=True
    )
    total_paid_so_far: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )
    remaining_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )

    # Guarantees
    guarantee_types: Mapped[str | None] = mapped_column(
        String(200), nullable=True
    )  # comma-separated: GOOD_JOB,PREPAYMENT
    guarantees_valid: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    mrs: Mapped[str | None] = mapped_column(String(50), nullable=True)

    # Payment method
    payment_method: Mapped[str | None] = mapped_column(String(30), nullable=True)
    payment_method_desc: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Description
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    project: Mapped["Main_project"] = relationship()
    contract: Mapped["Contract"] = relationship()
