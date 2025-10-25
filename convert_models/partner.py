from typing import List
from .base import Base
from sqlalchemy import   String
from sqlalchemy.orm import relationship,Mapped, mapped_column



class Partner(Base):
    __tablename__ = "partner"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    full_name : Mapped[str] = mapped_column(String(100))
    national_id : Mapped[str | None] = mapped_column(String(20))
    economic_code : Mapped[str | None] = mapped_column(String(20))
    is_legal_entity : Mapped[bool]
    address : Mapped[str] = mapped_column(String(200))
    is_vendor : Mapped[bool]
    is_contructor : Mapped[bool]
    bank_account : Mapped[List["Bank_Account"]] = relationship(back_populates="partner")
    pre_contract : Mapped[List["Pre_contract"]] = relationship(back_populates="partner")
