from sqlalchemy import Column, Integer, String,UniqueConstraint
from typing import List, Optional
from .base import Base

from sqlalchemy.orm import relationship,Mapped, mapped_column


class Activity(Base):
    __tablename__ = "activity"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30),unique=True,index=True)
    user_project_permission : Mapped[List["UserProjectPermission"]] = relationship(back_populates="activity")