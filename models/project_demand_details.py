import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, List
from sqlalchemy import Date, ForeignKey, Identity, Numeric, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .project_demand import Project_demand
    from .demand_document import Demand_document


class Project_demand_details(Base):
    """مدل جزئیات تقاضای پروژه - Project Demand Details"""

    __tablename__ = "project_demand_details"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)

    document_demand_id = mapped_column(ForeignKey("demand_document.id"), index=True)

    qty: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    measurement_unit: Mapped[str] = mapped_column(String(30))
    project_demand_id: Mapped[int] = mapped_column(
        ForeignKey("project_demand.id"), index=True
    )
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("project_demand_details.id"), index=True, nullable=True
    )
    current_stage: Mapped[str | None] = mapped_column(String(100), nullable=True)
    next_stage: Mapped[str | None] = mapped_column(String(100), nullable=True)

    issue_date: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)

    # Relationships
    project_demand: Mapped["Project_demand"] = relationship(
        back_populates="project_demand_details"
    )

    # Self-referencing relationship
    parent: Mapped["Project_demand_details"] = relationship(
        back_populates="children", remote_side=[id], uselist=False
    )
    children: Mapped[List["Project_demand_details"]] = relationship(
        back_populates="parent"
    )
    demand_document: Mapped["Demand_document"] = relationship(
        back_populates="project_demand_details"
    )
