from sqlalchemy import ForeignKey, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Statement_items(Base):
    """مدل اقلام صورت وضعیت - Statement Items"""

    __tablename__ = "statement_items"

    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    statement_id: Mapped[int] = mapped_column(ForeignKey("statement.id"), index=True)
    contract_item_id: Mapped[int] = mapped_column(
        ForeignKey("contract_item.id"), index=True
    )
    qty: Mapped[int]

    # Relationships
    statement: Mapped["Statement"] = relationship(back_populates="statement_items")
    contract_item: Mapped["Contract_item"] = relationship(
        back_populates="statement_items"
    )
