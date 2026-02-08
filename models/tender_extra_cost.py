from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Index, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .demand_document import Demand_document
    from .extra_cost import Extra_Cost


class Tender_Extra_Cost(Base):
    """مدل هزینه‌های جانبی مناقصه - Tender Extra Costs"""

    __tablename__ = "tender_extra_cost"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    tender_id: Mapped[int] = mapped_column(ForeignKey("demand_document.id"), index=True)
    extracost_id: Mapped[int] = mapped_column(ForeignKey("extra_cost.id"), index=True)

    # Relationships
    tender: Mapped["Demand_document"] = relationship(
        back_populates="tender_extra_costs"
    )
    extra_cost: Mapped["Extra_Cost"] = relationship(back_populates="tender_extra_costs")

    __table_args__ = (Index("idx_tender_extracost", "tender_id", "extracost_id"),)
