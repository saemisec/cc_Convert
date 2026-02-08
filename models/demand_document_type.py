from typing import TYPE_CHECKING, List
from sqlalchemy import Identity, String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

# No TYPE_CHECKING imports needed as workflow relationships removed


class Demand_document_type(Base):
    """مدل نوع سند تقاضا - Demand Document Type"""

    __tablename__ = "demand_document_type"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))

    # Relationships
    demand_documents: Mapped[List["Demand_document"]] = relationship(
        back_populates="document_type"
    )

    __table_args__ = (UniqueConstraint("title", name="uq_demand_document_type_title"),)
