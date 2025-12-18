import datetime
from decimal import Decimal
from sqlalchemy import Numeric, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.pre_contract import Pre_contract
from .base import Base


class Statement(Base):
    __tablename__ = "statement"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    contract_id: Mapped[int] = mapped_column(ForeignKey("pre_contract.id"), index=True)
    number: Mapped[str | None] = mapped_column(String(35))
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    register_date: Mapped[datetime.date | None]
    statement_date: Mapped[datetime.date | None]
    pre_contract: Mapped[Pre_contract] = relationship(back_populates="statement")

    # cbs_relation : relationship("Cbs",back_populates="main_project_relation")
