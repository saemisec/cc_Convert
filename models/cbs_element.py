from typing import List, Optional
from .base import Base
from sqlalchemy import REAL, Integer, String,BigInteger, String, ForeignKey,FLOAT
from sqlalchemy.orm import relationship,Mapped, mapped_column
from .cbs_type import Cbs_type
from .main_project import Main_project


class Cbs_element(Base):
    __tablename__ = "cbs_element"
    id : Mapped[int] = mapped_column(BigInteger,primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    title : Mapped[str] = mapped_column(String(100))
    parent_id : Mapped[int | None] = mapped_column(BigInteger,ForeignKey("cbs_element.id", ondelete="RESTRICT"),index=True)
    amount_irr : Mapped[float] =  mapped_column(REAL(precision=2, asdecimal=False))
    amount_cur : Mapped[float] =  mapped_column(REAL(precision=2, asdecimal=False))
    element_type : Mapped[int | None] = mapped_column(ForeignKey("cbs_type.id"),index=True)
    main_project_id : Mapped[int] = mapped_column(ForeignKey("main_project.id"),index=True)
    code : Mapped[str] = mapped_column(String(30))
    rev_no : Mapped[int]
    root_weighted_irr : Mapped[float] = mapped_column(REAL(precision=2, asdecimal=False))
    root_weighted_cur : Mapped[float] = mapped_column(REAL(precision=2, asdecimal=False))
    parent = relationship("Cbs_element", remote_side=[id], backref="children")
    cbs_type : Mapped[Cbs_type] = relationship(back_populates="cbs_element")
    main_project : Mapped[Main_project] = relationship(back_populates="cbs_element")
    contract_item : Mapped[List["Contract_item"]] = relationship(back_populates="cbs_element")
    addenum_item : Mapped[List["Addenum_item"]] = relationship(back_populates="cbs_element")
