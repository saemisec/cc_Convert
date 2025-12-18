import datetime
from decimal import Decimal
from sqlalchemy import Numeric, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .main_project import Main_project
from .base import Base


class Main_addendum(Base):
    __tablename__ = "main_addendum"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    main_project_id: Mapped[int] = mapped_column(ForeignKey("main_project.id"))
    title: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[datetime.date]
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=True)
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=True)
    duration: Mapped[int]
    end_date: Mapped[datetime.date]
    reg_date: Mapped[datetime.date]
    cbs_assign: Mapped[bool] = mapped_column(default=False, nullable=False)
    main_project: Mapped[Main_project] = relationship(
        back_populates="main_addendum", lazy="selectin"
    )
