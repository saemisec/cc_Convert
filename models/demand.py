import enum
from typing import TYPE_CHECKING, List
from sqlalchemy import String, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .project_demand import Project_demand


class Demand_item_type(enum.Enum):
    TAG_NO = "tag_no"
    CODEBASE = "code_base"


class Demand(Base):
    """مدل تقاضا - Demand"""

    __tablename__ = "demand"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)

    code: Mapped[str] = mapped_column(String(50), index=True)
    title: Mapped[str] = mapped_column(String(200))
    item_type: Mapped[Demand_item_type]

    # Relationships
    project_demands: Mapped[List["Project_demand"]] = relationship(
        back_populates="demand"
    )
