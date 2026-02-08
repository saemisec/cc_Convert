from typing import TYPE_CHECKING, List
from sqlalchemy import String, Identity, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .mdr_extra_cost import MdrExtraCost


class MdrExtraCostType(Base):
    """مدل انواع هزینه‌های اضافی MDR - MDR Extra Cost Types"""

    __tablename__ = "mdr_extra_cost_type"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(30), unique=True)

    # Relationships
    mdr_extra_costs: Mapped[List["MdrExtraCost"]] = relationship(
        back_populates="mdr_extra_cost_type"
    )

    __table_args__ = (UniqueConstraint("name", name="uq_mdr_extra_cost_type_name"),)
