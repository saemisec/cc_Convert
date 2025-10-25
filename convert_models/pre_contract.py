import datetime
import enum
from .base import Base
from .contract import Contract
from .main_phase import Main_phase
from .second_phase import Second_Phase
from .main_project import Main_project
from .partner import Partner
from .currency import Currency
from typing import List
from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship,Mapped, mapped_column, mapped_column



class Contract_status(enum.Enum):
    INPROGRESS = "InProgress"
    CANCELED = "Canceled"
    TOCONTRACT = "ToContract"


class Pre_contract(Base):
    __tablename__ = "pre_contract"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    title : Mapped[str] = mapped_column(String(500))
    partner_id : Mapped[int] = mapped_column(ForeignKey("partner.id"),index=True)
    main_project_id : Mapped[int] = mapped_column(ForeignKey("main_project.id"),index=True)
    number : Mapped[str] = mapped_column(String(50))
    request_number : Mapped[str] = mapped_column(String(30))
    amount_irr : Mapped[int | None] = mapped_column(BigInteger)
    amount_cur : Mapped[int | None] = mapped_column(BigInteger)
    register_date : Mapped[datetime.date]
    register_duration : Mapped[int]
    contract_status : Mapped[Contract_status]
    currency_id : Mapped[int | None] = mapped_column(ForeignKey("currency.id"),index=True)
    main_phase_id : Mapped[int | None] = mapped_column(ForeignKey("main_phase.id"),index=True)
    second_phase_id : Mapped[int | None] = mapped_column(ForeignKey("second_phase.id"),index=True)
    contract : Mapped[Contract] = relationship(back_populates="pre_contract",
                                                 uselist=False,single_parent=True)
    main_project : Mapped[Main_project] = relationship(back_populates="pre_contract")
    partner : Mapped[Partner] = relationship(back_populates="pre_contract")
    currency : Mapped[Currency] = relationship(back_populates="pre_contract")
    main_phase : Mapped[Main_phase] = relationship(back_populates="pre_contract")
    second_phase : Mapped[Second_Phase] = relationship(back_populates="pre_contract")
    #addendum : Mapped[List["Addendum"]] = relationship(back_populates="pre_contract")
    
