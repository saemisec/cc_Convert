import datetime
from decimal import Decimal
from sqlalchemy import Date, Identity, Numeric, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .main_project import Main_project
from .base import Base


class Main_addendum(Base):
    __tablename__ = "main_addendum"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    main_project_id: Mapped[int] = mapped_column(ForeignKey("main_project.id"))
    title: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[datetime.date]
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=True)
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=True)
    duration: Mapped[int]
    end_date: Mapped[datetime.date]
    reg_date: Mapped[datetime.date] = mapped_column(Date, default=datetime.date.today)
    cbs_assign: Mapped[bool] = mapped_column(default=False, nullable=False)
    main_project: Mapped[Main_project] = relationship(
        back_populates="main_addendum", lazy="selectin"
    )
