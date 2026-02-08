from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Identity, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .demand_document import Demand_document
    from .partner import Partner


class Bidder_list(Base):
    """مدل لیست شرکت کنندگان در مناقصه - Bidder List"""

    __tablename__ = "bidder_list"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(
        ForeignKey("demand_document.id"), index=True
    )
    partner_id: Mapped[int] = mapped_column(ForeignKey("partner.id"), index=True)
    is_winner: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = (
        UniqueConstraint(
            "document_id", "partner_id", name="uq_bidder_list_document_partner"
        ),
    )

    # Relationships
    demand_document: Mapped["Demand_document"] = relationship(
        back_populates="bidder_lists"
    )
    partner: Mapped["Partner"] = relationship(back_populates="bidder_lists")
