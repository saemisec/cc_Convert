import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import Date, String, ForeignKey, Identity, Boolean, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


if TYPE_CHECKING:
    from models.project_demand_details import Project_demand_details
    from models.demand_document_type import Demand_document_type
    from models.main_project import Main_project
    from models.bidder_list import Bidder_list
    from models.tender_extra_cost import Tender_Extra_Cost
    from models.contract import Contract


class Demand_document(Base):
    """مدل سند تقاضا - Demand Document"""

    __tablename__ = "demand_document"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    document_type_id: Mapped[int] = mapped_column(
        ForeignKey("demand_document_type.id"), index=True
    )

    mian_project_id: Mapped[int] = mapped_column(
        ForeignKey("main_project.id"), index=True
    )

    issue_date: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)

    avl_need: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default="false"
    )

    # Self-referencing foreign key to track document chain (e.g., Purchase Order → Tender → Contract Request)
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("demand_document.id"), index=True, nullable=True
    )

    # فیلد JSON برای ذخیره موقت داده‌های اعلام برنده مناقصه
    winner_announcement_data: Mapped[dict | None] = mapped_column(
        JSON, nullable=True, default=None
    )

    # Relationships
    document_type: Mapped["Demand_document_type"] = relationship(
        back_populates="demand_documents"
    )

    project: Mapped["Main_project"] = relationship(back_populates="demand_documents")

    project_demand_details: Mapped[List["Project_demand_details"]] = relationship(
        back_populates="demand_document"
    )

    bidder_lists: Mapped[List["Bidder_list"]] = relationship(
        back_populates="demand_document"
    )

    tender_extra_costs: Mapped[List["Tender_Extra_Cost"]] = relationship(
        back_populates="tender"
    )

    # Self-referencing relationship for document chain
    parent: Mapped["Demand_document | None"] = relationship(
        remote_side=[id], back_populates="children", foreign_keys=[parent_id]
    )
    children: Mapped[List["Demand_document"]] = relationship(
        back_populates="parent", foreign_keys="Demand_document.parent_id"
    )

    # Contracts created from this demand_document
    contracts: Mapped[List["Contract"]] = relationship(back_populates="demand_document")

    # purchase_request: Mapped["Purchase_request"] = relationship(
    #     back_populates="demand_document", uselist=False
    # )
