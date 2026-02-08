import datetime
from decimal import Decimal
from typing import List
from sqlalchemy import Date, Identity, Numeric, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .cbs_element import Cbs_element
from .pre_contract import Pre_contract
from .base import Base


class Contract_item(Base):
    __tablename__ = "contract_item"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    cbs_element_id: Mapped[int] = mapped_column(
        ForeignKey("cbs_element.id"), index=True
    )
    contract_id: Mapped[int] = mapped_column(ForeignKey("pre_contract.id"), index=True)
    local_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    foreign_amout: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    register_date: Mapped[datetime.date] = mapped_column(
        Date, default=datetime.date.today
    )
    # project_demand_id: Mapped[int | None] = mapped_column(
    #     ForeignKey("project_demand.id"), index=True, nullable=True
    # )

    # Relationships
    # cbs_element: Mapped[Cbs_element] = relationship(back_populates="contract_item")
    # pre_contract: Mapped[Pre_contract] = relationship(back_populates="contract_item")
    # contract_item_history: Mapped[List["Contract_item_history"]] = relationship(
    #     back_populates="contract_item"
    # )
    # project_demand: Mapped["Project_demand"] = relationship(
    #     back_populates="contract_items"
    # )
    # statement_items: Mapped[List["Statement_items"]] = relationship(
    #     back_populates="contract_item"
    # )
