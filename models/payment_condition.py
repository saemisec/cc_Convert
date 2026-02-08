from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import String, Numeric, ForeignKey, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .contract import Contract


class Payment_Condition(Base):
    """مدل شرایط پرداخت پیمان - Payment Condition model for contract payment terms"""

    __tablename__ = "payment_condition"

    # Primary key with Identity
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)

    # Foreign key to contract
    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"), index=True)

    # Fields
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    percentage: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    sequence_order: Mapped[int]

    # Relationship
    contract: Mapped["Contract"] = relationship(back_populates="payment_conditions")
