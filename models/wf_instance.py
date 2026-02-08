import enum
import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import (
    Identity,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Enum,
    Index,
    func,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .wf_template import WfTemplate
    from .wf_step import WfStep
    from .wf_task import WfTask
    from .wf_action_log import WfActionLog
    from .user import User


class InstanceStatus(enum.Enum):
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class WfInstance(Base):
    """Running instance of a workflow for a specific document - نمونه اجرایی گردش کار"""

    __tablename__ = "wf_instance"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    template_id: Mapped[int] = mapped_column(ForeignKey("wf_template.id"), index=True)
    entity_type: Mapped[str] = mapped_column(String(50))
    entity_id: Mapped[int] = mapped_column(Integer)
    current_step_id: Mapped[int | None] = mapped_column(
        ForeignKey("wf_step.id"), nullable=True
    )
    status: Mapped[InstanceStatus] = mapped_column(
        Enum(InstanceStatus, name="instance_status_enum"),
        default=InstanceStatus.IN_PROGRESS,
    )
    started_by_user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    started_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    completed_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    # Relationships
    template: Mapped["WfTemplate"] = relationship(back_populates="instances")
    current_step: Mapped["WfStep | None"] = relationship()
    started_by: Mapped["User"] = relationship()
    tasks: Mapped[List["WfTask"]] = relationship(back_populates="instance")
    action_logs: Mapped[List["WfActionLog"]] = relationship(
        back_populates="instance", order_by="WfActionLog.performed_at"
    )

    __table_args__ = (Index("idx_wf_instance_entity", "entity_type", "entity_id"),)
