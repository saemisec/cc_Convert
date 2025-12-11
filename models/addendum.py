import datetime
from .base import Base
from sqlalchemy import String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, mapped_column


class Addendum(Base):
    __tablename__ = "addendum"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    title : Mapped[str] = mapped_column(String(100))
    pre_contract_id :  Mapped[int] = mapped_column(ForeignKey("pre_contract.id"))
    rev_no : Mapped[int]
    revdate : Mapped[datetime.date]
    revdesc : Mapped[str | None] = mapped_column(String(100))
    amount_extend_irr : Mapped[int | None]
    amount_extend_cur : Mapped[int | None]
    date_extend : Mapped[int | None]
    RegDate : Mapped[datetime.date]
    pre_contract: Mapped["Pre_contract"] = relationship(back_populates="addendum")
