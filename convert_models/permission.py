from typing import List
from sqlalchemy import String
from sqlalchemy.orm import relationship,Mapped, mapped_column
from .base import Base



class Permission(Base):
    __tablename__ = "permission"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30),unique=True,index=True)
    user_project_permission : Mapped[List["UserProjectPermission"]] = relationship(back_populates="permission")