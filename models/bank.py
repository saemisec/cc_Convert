from typing import List
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base


class Bank(Base):
    __tablename__ = "bank"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    name: Mapped[str] = mapped_column(String(30), unique=True)
    bank_account: Mapped[List["Bank_Account"]] = relationship(back_populates="bank")
    __table_args__ = (UniqueConstraint("name", name="uq_bank_name"),)
