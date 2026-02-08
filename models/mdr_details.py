import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Identity, String, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

if TYPE_CHECKING:
    from models.mdr import Mdr


class Mdr_details(Base):
    __tablename__ = "mdr_details"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    mdr_id: Mapped[int] = mapped_column(ForeignKey("mdr.id"), index=True)
    rev: Mapped[str] = mapped_column(String(20))
    receipt_date: Mapped[datetime.date | None] = mapped_column(Date)
    disk_id: Mapped[str] = mapped_column(String(4))
    files: Mapped[str] = mapped_column(String(100))

    __table_args__ = (UniqueConstraint("mdr_id", "rev", name="uq_mdr_details_id_rev"),)

    # Relationship
    mdr: Mapped["Mdr"] = relationship(back_populates="mdr_details")
