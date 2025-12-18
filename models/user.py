from typing import Optional, List
from sqlalchemy import String, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(60), index=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(120), default=None)
    email: Mapped[Optional[str]] = mapped_column(String(120), index=True, default=None)
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_management: Mapped[bool] = mapped_column(Boolean, default=True)

    refresh_token: Mapped[List["RefreshToken"]] = relationship(back_populates="user")
    user_position: Mapped[List["User_position"]] = relationship(back_populates="user")

    __table_args__ = (
        UniqueConstraint("username", name="uq_user_username"),
        UniqueConstraint("email", name="uq_user_email"),
    )
