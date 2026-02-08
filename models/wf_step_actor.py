from typing import TYPE_CHECKING
from sqlalchemy import Identity, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .wf_step import WfStep
    from .position import Position


class WfStepActor(Base):
    """Position assigned to act on a workflow step - مسئول مرحله"""

    __tablename__ = "wf_step_actor"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    step_id: Mapped[int] = mapped_column(ForeignKey("wf_step.id"), index=True)
    position_id: Mapped[int] = mapped_column(ForeignKey("position.id"), index=True)

    # Relationships
    step: Mapped["WfStep"] = relationship(back_populates="actors")
    position: Mapped["Position"] = relationship()

    __table_args__ = (
        UniqueConstraint("step_id", "position_id", name="uq_wf_step_actor"),
    )
