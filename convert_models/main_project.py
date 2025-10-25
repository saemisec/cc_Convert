import datetime
from typing import List
from .base import Base
from convert_models.currency import Currency
from convert_models.employee import Employee
from sqlalchemy import Column, Integer, BigInteger, String, Date, ForeignKey,UniqueConstraint
from sqlalchemy.sql import case
from sqlalchemy.orm import relationship , Mapped, mapped_column, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property


class Main_project(Base):
    __tablename__ = "main_project"
    id : Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    old_id : Mapped[int | None]
    employee_id : Mapped[int] = mapped_column(ForeignKey("employee.id"),index=True)
    title : Mapped[str] = mapped_column(String(100))
    number : Mapped[str | None] = mapped_column(String(20))
    Abbreviation : Mapped[str] = mapped_column(String(5))
    workshop_no : Mapped[str | None] = mapped_column(String(10))
    agreement_number : Mapped[str | None] = mapped_column(String(10))
    amount_irr : Mapped[int | None] = mapped_column(BigInteger)
    amount_cur : Mapped[int | None] = mapped_column(BigInteger)
    currency_id : Mapped[int | None] = mapped_column(ForeignKey("currency.id"),index=True)
    start_date : Mapped[datetime.date | None]
    contract_date : Mapped[datetime.date | None]
    inform_date : Mapped[datetime.date | None]
    dl_date : Mapped[datetime.date | None]
    duration : Mapped[int | None]
    is_cost_center : Mapped[bool]
    contract_type : Mapped[str | None] = mapped_column(String(20))
    adjustment : Mapped[str | None] = mapped_column(String(20))
    adjustment_desc : Mapped[str | None] = mapped_column(String(50))
    insu_percent : Mapped[int | None]
    tax_percent : Mapped[int | None]
    good_job_percent : Mapped[int | None]
    has_customs_duties : Mapped[bool]
    customs_duties_desc :  Mapped[str | None]
    insurance_policy : Mapped[bool]
    insurance_policy_desc : Mapped[str | None]
    is_final : Mapped[bool]
    __table_args__ = (UniqueConstraint("Abbreviation", name="uq_Abbreviation"),)
    currency: Mapped[Currency] = relationship(back_populates="main_project")
    employee: Mapped[Employee] = relationship(back_populates="main_project")
    pre_contract : Mapped[List["Pre_contract"]] = relationship(back_populates="main_project")
    user_project_permission : Mapped[List["UserProjectPermission"]] = relationship(back_populates="main_project")
    #cbs_relation : relationship("Cbs",back_populates="main_project_relation")

    @hybrid_property
    def status(self):
        pass
        #return 'خاتمه یافته' if self.is_final else 'در جریان'
    
    @status.expression
    def status(cls):
        return case(
            (cls.is_final,'خاتمه یافته'),
            else_=('در جریان'),
        )
    
    @hybrid_property
    def project_type(self):
        pass
        #return 'خاتمه یافته' if self.is_final else 'در جریان'
    
    
        
