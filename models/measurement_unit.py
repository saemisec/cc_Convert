from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship,Mapped, mapped_column


class Measurement_unit(Base):
    __tablename__ = "measurement_unit"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    name : Mapped[str] = mapped_column(String(30),unique=True)
    code : Mapped[str] = mapped_column(String(10),unique=True)
    is_nemeric : Mapped[bool]
