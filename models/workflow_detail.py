from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey, Identity, Index
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .workflow import Workflow
    from .work_flow_stage import Work_flow_stage


class Workflow_detail(Base):
    """مدل جزئیات گردش کار - Workflow Detail"""

    __tablename__ = "workflow_detail"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    workflow_id: Mapped[int] = mapped_column(ForeignKey("workflow.id"), index=True)
    from_stage_id: Mapped[int] = mapped_column(
        ForeignKey("work_flow_stage.id"), index=True
    )
    to_stage_id: Mapped[int] = mapped_column(
        ForeignKey("work_flow_stage.id"), index=True
    )
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("workflow_detail.id"), index=True, nullable=True
    )

    # Relationships
    workflow: Mapped["Workflow"] = relationship(back_populates="workflow_details")
    from_stage: Mapped["Work_flow_stage"] = relationship(
        back_populates="workflow_details_from", foreign_keys=[from_stage_id]
    )
    to_stage: Mapped["Work_flow_stage"] = relationship(
        back_populates="workflow_details_to", foreign_keys=[to_stage_id]
    )

    # Self-referential relationship for parent/children
    parent: Mapped["Workflow_detail | None"] = relationship(
        back_populates="children", remote_side=[id], foreign_keys=[parent_id]
    )
    children: Mapped[List["Workflow_detail"]] = relationship(
        back_populates="parent", foreign_keys=[parent_id]
    )

    __table_args__ = (
        Index(
            "idx_workflow_detail_from_to",
            "from_stage_id",
            "to_stage_id",
        ),
    )
