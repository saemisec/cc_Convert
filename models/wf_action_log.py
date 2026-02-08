import enum
import datetime
from typing import TYPE_CHECKING
from sqlalchemy import (
    Identity,
    Text,
    ForeignKey,
    DateTime,
    Enum,
    JSON,
    func,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .wf_instance import WfInstance
    from .wf_step import WfStep
    from .user import User


class ActionType(enum.Enum):
    STARTED = "started"
    APPROVED = "approved"
    REJECTED = "rejected"
    RETURNED = "returned"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class WfActionLog(Base):
    """Audit log for all workflow actions - لاگ عملیات گردش کار"""

    __tablename__ = "wf_action_log"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    instance_id: Mapped[int] = mapped_column(ForeignKey("wf_instance.id"), index=True)
    step_id: Mapped[int | None] = mapped_column(ForeignKey("wf_step.id"), nullable=True)
    action: Mapped[ActionType] = mapped_column(
        Enum(ActionType, name="action_type_enum")
    )
    performed_by_user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    performed_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    extra_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    # Relationships
    instance: Mapped["WfInstance"] = relationship(back_populates="action_logs")
    step: Mapped["WfStep | None"] = relationship()
    performed_by: Mapped["User"] = relationship()
