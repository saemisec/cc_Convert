from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Identity, Index
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .mdr import Mdr
    from .mdr_extra_cost_type import MdrExtraCostType


class MdrExtraCost(Base):
    """مدل هزینه‌های اضافی MDR - MDR Extra Costs"""

    __tablename__ = "mdr_extra_cost"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    mdr_id: Mapped[int] = mapped_column(ForeignKey("mdr.id"), index=True)
    mdr_extra_cost_type_id: Mapped[int] = mapped_column(
        ForeignKey("mdr_extra_cost_type.id"), index=True
    )

    # Relationships

    mdr: Mapped["Mdr"] = relationship(
        foreign_keys=[mdr_id], back_populates="mdr_extra_cost"
    )
    mdr_extra_cost_type: Mapped["MdrExtraCostType"] = relationship(
        back_populates="mdr_extra_costs"
    )

    __table_args__ = (Index("idx_mdr_extra_cost_mdr", "mdr_id"),)
