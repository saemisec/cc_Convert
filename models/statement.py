import datetime
from typing import List
from models.contract import Contract
from sqlalchemy import BigInteger, String, ForeignKey,UniqueConstraint
from sqlalchemy.sql import case
from sqlalchemy.orm import relationship , Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base


class Statement(Base):
    __tablename__ = "statement"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    contract_id : Mapped[int] = mapped_column(ForeignKey("contract.id"),index=True)
    number : Mapped[str | None] = mapped_column(String(35))
    amount_irr : Mapped[int | None] = mapped_column(BigInteger)
    amount_cur : Mapped[int | None] = mapped_column(BigInteger)
    register_date : Mapped[datetime.date | None]
    statement_date : Mapped[datetime.date | None]
    contract : Mapped[Contract] = relationship(back_populates="statement")
    
    
    
    
    #cbs_relation : relationship("Cbs",back_populates="main_project_relation")

    