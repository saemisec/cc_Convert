import datetime
from decimal import Decimal
from typing import List
from sqlalchemy import Numeric, String, ForeignKey, UniqueConstraint
from sqlalchemy.sql import case
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from models.currency import Currency
from models.employee import Employee
from .base import Base


class Main_project(Base):
    __tablename__ = "main_project"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id: Mapped[int | None]
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), index=True)
    title: Mapped[str] = mapped_column(String(100))
    number: Mapped[str | None] = mapped_column(String(20))
    Abbreviation: Mapped[str] = mapped_column(String(5))
    workshop_no: Mapped[str | None] = mapped_column(String(10))
    agreement_number: Mapped[str | None] = mapped_column(String(10))
    amount_irr: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    amount_cur: Mapped[Decimal] = mapped_column(Numeric(18, 2))
    currency_id: Mapped[int | None] = mapped_column(
        ForeignKey("currency.id"), index=True
    )
    start_date: Mapped[datetime.date | None]
    contract_date: Mapped[datetime.date | None]
    inform_date: Mapped[datetime.date | None]
    end_date: Mapped[datetime.date | None]
    dl_date: Mapped[datetime.date | None]
    duration: Mapped[int | None]
    is_cost_center: Mapped[bool]
    contract_type: Mapped[str | None] = mapped_column(String(20))
    adjustment: Mapped[str | None] = mapped_column(String(20))
    adjustment_desc: Mapped[str | None] = mapped_column(String(50))
    insu_percent: Mapped[int | None]
    tax_percent: Mapped[int | None]
    good_job_percent: Mapped[int | None]
    has_customs_duties: Mapped[bool]
    customs_duties_desc: Mapped[str | None]
    insurance_policy: Mapped[bool]
    insurance_policy_desc: Mapped[str | None]
    cbs_assign: Mapped[bool] = mapped_column(default=False, nullable=True)

    is_final: Mapped[bool]
    __table_args__ = (UniqueConstraint("Abbreviation", name="uq_Abbreviation"),)
    currency: Mapped[Currency] = relationship(back_populates="main_project")
    employee: Mapped[Employee] = relationship(back_populates="main_project")
    pre_contract: Mapped[List["Pre_contract"]] = relationship(
        back_populates="main_project"
    )

    cbs_element: Mapped[List["Cbs_element"]] = relationship(
        back_populates="main_project"
    )

    # permission: Mapped[List["Permission"]] = relationship(back_populates="main_project")
    mdr: Mapped[List["Mdr"]] = relationship(back_populates="main_project")
    project_demands: Mapped[List["Project_demand"]] = relationship(
        back_populates="project"
    )

    demand_documents: Mapped[List["Demand_document"]] = relationship(
        back_populates="project"
    )

    main_addendum: Mapped[List["Main_addendum"]] = relationship(
        back_populates="main_project", lazy="selectin"
    )
    # purchase_requests: Mapped[List["Purchase_request"]] = relationship(
    #     back_populates="main_project"
    # )
    # tenders: Mapped[List["Tender"]] = relationship(back_populates="main_project")
    # inqueries: Mapped[List["Inquery"]] = relationship(back_populates="main_project")
    # tbe_requests: Mapped[List["TBE_Request"]] = relationship(
    #     back_populates="main_project"
    # )

    @hybrid_property
    def status(self):
        pass
        # return 'خاتمه یافته' if self.is_final else 'در جریان'

    @status.expression
    def status(cls):
        return case(
            (cls.is_final, "خاتمه یافته"),
            else_=("در جریان"),
        )

    @hybrid_property
    def project_type(self):
        pass
        # return 'خاتمه یافته' if self.is_final else 'در جریان'
