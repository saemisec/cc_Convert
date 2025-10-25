from typing import List
from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import relationship,Mapped, mapped_column

#from convert_models.main_project import Main_project

class Currency(Base):
    __tablename__ = "currency"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    name : Mapped[str] = mapped_column(String(20),unique=True)
    pre_contract : Mapped[List["Pre_contract"]] = relationship(back_populates="currency")
    main_project: Mapped[List["Main_project"]] = relationship(back_populates="currency")
