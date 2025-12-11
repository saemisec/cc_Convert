from typing import List, Optional
from .base import Base
from sqlalchemy import Integer, String,BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column
from .cbs_element import Cbs_element
from .addenum import Addenum
import datetime


class Addenum_item(Base):
    __tablename__ = "addenum_item"
    id : Mapped[int] = mapped_column(BigInteger,primary_key=True, index=True, autoincrement=True)
    cbs_element_id : Mapped[int] = mapped_column(ForeignKey("cbs_element.id"),index=True)
    addenum_id : Mapped[int] = mapped_column(ForeignKey("addenum.id"),index=True)
    local_amount : Mapped[int | None] = mapped_column(BigInteger)
    foreign_amout : Mapped[int | None] = mapped_column(BigInteger)
    register_date : Mapped[datetime.date]
    cbs_element : Mapped[Cbs_element] = relationship(back_populates="addenum_item")
    addenum : Mapped[Addenum] = relationship(back_populates="addenum_item")
    
