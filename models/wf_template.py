from typing import TYPE_CHECKING, List
import datetime
from sqlalchemy import Identity, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .wf_step import WfStep
    from .wf_instance import WfInstance


class WfTemplate(Base):
    """Workflow template definition - الگوی گردش کار"""

    __tablename__ = "wf_template"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    entity_type: Mapped[str] = mapped_column(String(50), index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    # Relationships
    steps: Mapped[List["WfStep"]] = relationship(
        back_populates="template", order_by="WfStep.step_order"
    )
    instances: Mapped[List["WfInstance"]] = relationship(back_populates="template")
