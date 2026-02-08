import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, List
import enum
from sqlalchemy import Date, Numeric, String, ForeignKey, Identity
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .contract import Contract
    from .main_phase import Main_phase
    from .second_phase import Second_Phase
    from .main_project import Main_project
    from .partner import Partner
    from .currency import Currency

    # from .statement import Statement
    # from .addendum import Addendum


class Contract_status(enum.Enum):
    INPROGRESS = "InProgress"
    CANCELED = "Canceled"
    TOCONTRACT = "ToContract"


class Pre_contract(Base):
    __tablename__ = "pre_contract"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    title: Mapped[str] = mapped_column(String(200))
    partner_id: Mapped[int] = mapped_column(ForeignKey("partner.id"), index=True)
    main_project_id: Mapped[int] = mapped_column(
        ForeignKey("main_project.id"), index=True
    )
    number: Mapped[str] = mapped_column(String(50))
    request_number: Mapped[str] = mapped_column(String(30))
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    register_date: Mapped[datetime.date] = mapped_column(
        Date, default=datetime.date.today
    )
    register_duration: Mapped[int]
    contract_status: Mapped[Contract_status]
    currency_id: Mapped[int | None] = mapped_column(
        ForeignKey("currency.id"), index=True
    )
    main_phase_id: Mapped[int | None] = mapped_column(
        ForeignKey("main_phase.id"), index=True
    )
    second_phase_id: Mapped[int | None] = mapped_column(
        ForeignKey("second_phase.id"), index=True
    )
    contract: Mapped["Contract"] = relationship(
        back_populates="pre_contract", uselist=False
    )
    main_project: Mapped["Main_project"] = relationship(back_populates="pre_contract")
    partner: Mapped["Partner"] = relationship(back_populates="pre_contract")
    currency: Mapped["Currency"] = relationship(back_populates="pre_contract")
    main_phase: Mapped["Main_phase"] = relationship(back_populates="pre_contract")
    second_phase: Mapped["Second_Phase"] = relationship(back_populates="pre_contract")
    # statement: Mapped[List["Statement"]] = relationship(
    #     back_populates="pre_contract", lazy="selectin"
    # )
    # contract_item: Mapped[List["Contract_item"]] = relationship(
    #     back_populates="pre_contract"
    # )
    # addendum: Mapped[List["Addendum"]] = relationship(back_populates="precontract")
