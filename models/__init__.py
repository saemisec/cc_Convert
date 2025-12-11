from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from .activity import Activity
from .addenum import Addenum
from .addenum_item import Addenum_item
from .bank_account import Bank_Account
from .bank import Bank
from .cbs_element import Cbs_element
from .cbs_type import Cbs_type
from .contract import Contract
from .contract_item import Contract_item
from .currency import Currency
from .delivery_type import Delivery_type
from .department import Department
from .employee import Employee
from .main_phase import Main_phase
from .main_project import Main_project
from .measurement_unit import Measurement_unit
from .partner import Partner
from .payment_condition import Payment_condition
from .permission import Permission
from .pre_contract import Pre_contract
from .refresh_token import RefreshToken
from .second_phase import Second_Phase
from .statement import Statement
from .user_project_permission import UserProjectPermission
from .user import User




class Base(AsyncAttrs, DeclarativeBase):
    pass


__all__ = ["Base",
           "Activity",
           "Addenum",
           "Addenum_item",
           "Bank_Account",
           "Bank",
           "Cbs_element",
           "Cbs_type",
           "Contract",
           "Contract_item",
           "Currency",
           "Delivery_type",
           "Department",
           "Employee",
           "Main_phase",
           "Main_project",
           "Measurement_unit",
           "Payment_condition",
           "Partner",
           "Permission",
           "Pre_contract",
           "RefreshToken",
           "Second_Phase",
           "Statement",
           "UserProjectPermission",
           "User"]
