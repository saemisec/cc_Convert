import enum
from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import String, Numeric, ForeignKey, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .contract import Contract


class Item_Type(enum.Enum):
    """نوع آیتم قرارداد - Contract Item Type"""

    MAIN_ITEM = "MAIN_ITEM"
    SPARE_PART = "SPARE_PART"
    EXTRA_COST = "EXTRA_COST"


class Contract_Item(Base):
    """مدل آیتم‌های پیمان - Contract Items model"""

    __tablename__ = "contract_item"

    # Primary key with Identity
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)

    # Foreign key to contract
    contract_id: Mapped[int] = mapped_column(ForeignKey("contract.id"), index=True)

    # Fields
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    item_type: Mapped[Item_Type]
    quantity: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    unit_price_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    unit_price_cur: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )
    total_price_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    total_price_cur: Mapped[Decimal | None] = mapped_column(
        Numeric(18, 2), nullable=True
    )

    # Relationship
    contract: Mapped["Contract"] = relationship(back_populates="contract_items")
