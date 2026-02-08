import enum
from typing import TYPE_CHECKING, List
from sqlalchemy import (
    Identity,
    String,
    Integer,
    Boolean,
    ForeignKey,
    UniqueConstraint,
    Enum,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .wf_template import WfTemplate
    from .wf_step_actor import WfStepActor
    from .wf_task import WfTask


class StepType(enum.Enum):
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"


class WfStep(Base):
    """Workflow step within a template - مرحله گردش کار"""

    __tablename__ = "wf_step"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    template_id: Mapped[int] = mapped_column(ForeignKey("wf_template.id"), index=True)
    name: Mapped[str] = mapped_column(String(200))
    step_order: Mapped[int] = mapped_column(Integer)
    step_type: Mapped[StepType] = mapped_column(
        Enum(StepType, name="step_type_enum"), default=StepType.SEQUENTIAL
    )
    can_reject: Mapped[bool] = mapped_column(Boolean, default=True)
    reject_to_step_id: Mapped[int | None] = mapped_column(
        ForeignKey("wf_step.id"), nullable=True
    )

    # Relationships
    template: Mapped["WfTemplate"] = relationship(back_populates="steps")
    actors: Mapped[List["WfStepActor"]] = relationship(back_populates="step")
    tasks: Mapped[List["WfTask"]] = relationship(back_populates="step")

    # Self-referential for reject target
    reject_to_step: Mapped["WfStep | None"] = relationship(
        remote_side=[id], foreign_keys=[reject_to_step_id]
    )

    __table_args__ = (
        UniqueConstraint("template_id", "step_order", name="uq_wf_step_order"),
    )
