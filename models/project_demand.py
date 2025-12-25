from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Project_demand(Base):
    __tablename__ = "project_demand"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("main_project.id"), nullable=False)
    good_id: Mapped[int] = mapped_column(ForeignKey("good.id"), nullable=False)
    qty: Mapped[int] = mapped_column(default=0, nullable=False)

    project: Mapped["Main_project"] = relationship()
    good: Mapped["Good"] = relationship()
