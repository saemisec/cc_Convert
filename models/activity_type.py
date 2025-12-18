from typing import List
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Activity_type(Base):
    __tablename__ = "activity"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, index=True)

    permission: Mapped[List["Permission"]] = relationship(
        back_populates="activity_type"
    )
