import datetime
from decimal import Decimal
import enum
from typing import TYPE_CHECKING, List
from sqlalchemy import Date, ForeignKey, Identity, Numeric, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .main_project import Main_project
    from .demand import Demand
    from .mr_item import MrItem


class Prj_DemandItemType(enum.Enum):
    MR_ITEM = "mr_item"
    GENERAL_ITEM = "general_item"


class Project_demand(Base):
    """مدل تقاضای پروژه - Project Demand"""

    __tablename__ = "project_demand"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("main_project.id"), index=True)
    demand_id: Mapped[int] = mapped_column(ForeignKey("demand.id"), index=True)
    # workflow_id: Mapped[int] = mapped_column(ForeignKey("workflow.id"), index=True)
    qty: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    measurement_unit_id: Mapped[int] = mapped_column(
        ForeignKey("measurement_unit.id"), index=True
    )
    item_type: Mapped[Prj_DemandItemType]

    item_per_set: Mapped[int | None] = mapped_column(nullable=True)
    total_qty_mu: Mapped[int] = mapped_column(
        ForeignKey("measurement_unit.id"), index=True, nullable=True
    )
    total_qty: Mapped[int]
    workflow: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    project: Mapped["Main_project"] = relationship(back_populates="project_demands")
    demand: Mapped["Demand"] = relationship(back_populates="project_demands")

    mr_item: Mapped["MrItem"] = relationship(
        back_populates="project_demand", uselist=False
    )

    issue_date: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)

    project_demand_details: Mapped[List["Project_demand_details"]] = relationship(
        back_populates="project_demand"
    )
    # contract_items: Mapped[List["Contract_item"]] = relationship(
    #     back_populates="project_demand"
    # )
