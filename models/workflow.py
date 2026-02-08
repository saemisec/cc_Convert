from typing import TYPE_CHECKING, List
from sqlalchemy import Identity, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .workflow_detail import Workflow_detail


class Workflow(Base):
    """مدل گردش کار - Workflow"""

    __tablename__ = "workflow"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))

    # Relationships
    workflow_details: Mapped[List["Workflow_detail"]] = relationship(
        back_populates="workflow"
    )
