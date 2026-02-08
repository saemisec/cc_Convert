from typing import Optional, List
from sqlalchemy import Identity, String, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from models.user import User
from .base import Base


class User_position(Base):
    __tablename__ = "user_position"
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    position_id: Mapped[int] = mapped_column(ForeignKey("position.id"), index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    user: Mapped["User"] = relationship(back_populates="user_position")
    position: Mapped["Position"] = relationship(back_populates="user_position")
    permission: Mapped[List["Permission"]] = relationship(
        back_populates="user_position"
    )

    __table_args__ = (
        UniqueConstraint("user_id", "position_id", name="uq_user_position_composite"),
    )
