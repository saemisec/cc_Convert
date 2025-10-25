from typing import Optional,List
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import relationship,Mapped, mapped_column
from .base import Base
from .department import Department




class User(Base):
    __tablename__ = "user"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(60), unique=True, index=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(120), default=None)
    email: Mapped[Optional[str]] = mapped_column(String(120), unique=True, index=True, default=None)
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_management: Mapped[bool] = mapped_column(Boolean, default=True)
    department_id: Mapped[Optional[int]] = mapped_column(ForeignKey("department.id"), index=True)
    department: Mapped[Department] = relationship(back_populates="user")
    refresh_token: Mapped[List["RefreshToken"]] = relationship(back_populates="user")
    user_project_permission : Mapped[List["UserProjectPermission"]] = relationship(back_populates="user")

    