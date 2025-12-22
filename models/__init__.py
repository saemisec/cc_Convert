from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from .activity_type import Activity_type
from .addendum import Addendum
from .bank_account import Bank_Account
from .bank import Bank
from .cbs_element import Cbs_element
from .cbs_element_history import Cbs_element_history
from .cbs_type import Cbs_type
from .contract import Contract
from .contract_item import Contract_item
from .contract_item_history import Contract_item_history
from .currency import Currency
from .delivery_type import Delivery_type
from .department import Department
from .employee import Employee
from .form_entity import Form_Entity
from .main_addendum import Main_addendum
from .main_phase import Main_phase
from .main_project import Main_project
from .mdr import Mdr
from .mdr_details import Mdr_details
from .measurement_unit import Measurement_unit
from .partner import Partner
from .payment_condition import Payment_condition
from .permission import Permission
from .position import Position
from .pre_contract import Pre_contract
from .refresh_token import RefreshToken
from .second_phase import Second_Phase
from .statement import Statement
from .user_position import User_position
from .user import User



class Base(AsyncAttrs, DeclarativeBase):
    pass


__all__ = [
    "Base",
    "Activity_type",
    "Addendum",
    "Bank_Account",
    "Bank",
    "Cbs_element",
    "Cbs_element_history",
    "Cbs_type",
    "Contract",
    "Contract_item",
    "Contract_item_history",
    "Currency",
    "Delivery_type",
    "Department",
    "Employee",
    "Form_Entity",
    "Main_addendum",
    "Main_phase",
    "Main_project",
    "Mdr_details",
    "Mdr",
    "Measurement_unit",
    "Payment_condition",
    "Partner",
    "Permission",
    "Position",
    "Pre_contract",
    "RefreshToken",
    "Second_Phase",
    "Statement",
    "User_position",
    "User",
    "SupAgreement",
    "SupAgreementType",
    "SupAmendment",
    "SupContractType",
    "SupContractor",
    "SupCostType",
    "SupCountry",
    "SupDeductionAgr",
    "SupEmployer",
    "SupMainCorp",
    "SupMainPrj",
    "SupMoein",
    "SupStatement",
    "SupStatementItem",
    "SupVouchStat",
    "SupVoucher",
]
