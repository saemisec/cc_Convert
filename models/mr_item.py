import enum
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .project_demand import Project_demand
    from .mdr import Mdr


class MR_item_type(enum.Enum):
    STANDARD = "standard"
    SPARE_PART = "spare_part"


class MrItem(Base):
    """مدل اقلام MR - MR Items"""

    __tablename__ = "mr_item"

    id: Mapped[int] = mapped_column(
        ForeignKey("project_demand.id"), primary_key=True, index=True
    )
    mdr_id: Mapped[int] = mapped_column(ForeignKey("mdr.id"), index=True)
    item_type: Mapped[MR_item_type] = mapped_column()
    related_datasheet_id: Mapped[int | None] = mapped_column(
        ForeignKey("mdr.id"), index=True, nullable=True
    )

    effective_rev: Mapped[str] = mapped_column(String(5), nullable=False)

    # Relationships
    project_demand: Mapped["Project_demand"] = relationship(
        back_populates="mr_item", uselist=False
    )
    mdr: Mapped["Mdr"] = relationship(foreign_keys=[mdr_id], back_populates="mr_items")

    related_datasheet: Mapped["Mdr"] = relationship(
        foreign_keys=[related_datasheet_id], back_populates="related_mr_items"
    )

    __table_args__ = (Index("idx_mdr_project", "mdr_id"),)
