import enum
import datetime
from typing import TYPE_CHECKING
from sqlalchemy import (
    Identity,
    Text,
    ForeignKey,
    DateTime,
    Enum,
    Index,
    func,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .wf_instance import WfInstance
    from .wf_step import WfStep
    from .position import Position
    from .user import User


class TaskStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class WfTask(Base):
    """Individual approval task assigned to a position - تسک تایید"""

    __tablename__ = "wf_task"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    instance_id: Mapped[int] = mapped_column(ForeignKey("wf_instance.id"), index=True)
    step_id: Mapped[int] = mapped_column(ForeignKey("wf_step.id"), index=True)
    position_id: Mapped[int] = mapped_column(ForeignKey("position.id"), index=True)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, name="task_status_enum"), default=TaskStatus.PENDING
    )
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    acted_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("user.id"), nullable=True
    )
    acted_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # Relationships
    instance: Mapped["WfInstance"] = relationship(back_populates="tasks")
    step: Mapped["WfStep"] = relationship(back_populates="tasks")
    position: Mapped["Position"] = relationship()
    acted_by: Mapped["User | None"] = relationship()

    __table_args__ = (Index("idx_wf_task_inbox", "instance_id", "status"),)
