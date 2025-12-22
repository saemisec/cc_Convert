import datetime
from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Date, Text, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.base import Base

if TYPE_CHECKING:
    from models.mdr import Mdr


class Mdr_details(Base):
    __tablename__ = "mdr_details"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    mdr_id: Mapped[int] = mapped_column(ForeignKey("mdr.id"), index=True)
    rev: Mapped[str] = mapped_column(String(20))
    receipt_date: Mapped[datetime.date | None] = mapped_column(Date)
    disk_id: Mapped[str] = mapped_column(String(4))
    files: Mapped[str] = mapped_column(Text)
    
    __table_args__ = (UniqueConstraint("mdr_id",  name="uq_mdr_details_id_rev"),)

    # Relationship
    mdr: Mapped["Mdr"] = relationship(back_populates="mdr_details")
