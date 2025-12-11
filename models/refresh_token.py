from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column,relationship
from .user import User
from .base import Base

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    jti: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False)
    expires_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), index=True)
    user: Mapped[User] = relationship(back_populates="refresh_token")
