from typing import TYPE_CHECKING, Optional, List
from sqlalchemy import Identity, String, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .user_position import User_position
    from .refresh_token import RefreshToken


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(60), index=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(120), default=None)
    email: Mapped[Optional[str]] = mapped_column(String(120), index=True, default=None)
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_management: Mapped[bool] = mapped_column(Boolean, default=True)
    refresh_token: Mapped[List["RefreshToken"]] = relationship(back_populates="user")
    user_position: Mapped[List["User_position"]] = relationship(back_populates="user")

    # ledgers: Mapped[List["Ledger"]] = relationship(
    #     foreign_keys="Ledger.created_by", back_populates="creator"
    # )

    __table_args__ = (
        UniqueConstraint("username", name="uq_user_username"),
        UniqueConstraint("email", name="uq_user_email"),
    )
