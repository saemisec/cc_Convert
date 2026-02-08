from typing import TYPE_CHECKING, List
from sqlalchemy import String, UniqueConstraint, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .tender_extra_cost import Tender_Extra_Cost


class Extra_Cost(Base):
    """مدل هزینه‌های جانبی - Extra Costs"""

    __tablename__ = "extra_cost"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    old_id: Mapped[int | None] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    # Relationships
    tender_extra_costs: Mapped[List["Tender_Extra_Cost"]] = relationship(
        back_populates="extra_cost"
    )

    __table_args__ = (UniqueConstraint("name", name="uq_extra_cost_name"),)
