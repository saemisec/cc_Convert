from typing import TYPE_CHECKING, List
from sqlalchemy import String, Identity, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .workflow_detail import Workflow_detail


class Work_flow_stage(Base):
    """مدل مرحله گردش کار - Workflow Stage"""

    __tablename__ = "work_flow_stage"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))

    # Relationships
    workflow_details_from: Mapped[List["Workflow_detail"]] = relationship(
        back_populates="from_stage",
        foreign_keys="[Workflow_detail.from_stage_id]",
    )
    workflow_details_to: Mapped[List["Workflow_detail"]] = relationship(
        back_populates="to_stage",
        foreign_keys="[Workflow_detail.to_stage_id]",
    )

    __table_args__ = (UniqueConstraint("title", name="uq_work_flow_stage_title"),)
