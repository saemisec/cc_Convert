from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

from .activity_type import Activity_type

# from .addendum import Addendum
from .bank_account import Bank_Account
from .bank import Bank

# from .bidders_document import Bidders_Document
from .bidder_list import Bidder_list
from .cbs_element import Cbs_element

# from .cbs_element_history import Cbs_element_history
from .cbs_type import Cbs_type

from .contract import Contract
from .contract_item import Contract_Item

# from .contract_item_history import Contract_item_history
from .currency import Currency
from .delivery_type import Delivery_type

from .demand import Demand

from .demand_document import Demand_document

from .demand_document_type import Demand_document_type
from .department import Department
from .employee import Employee
from .extra_cost import Extra_Cost

from .form_entity import Form_Entity

from .main_addendum import Main_addendum
from .main_phase import Main_phase
from .main_project import Main_project
from .mdr import Mdr

from .mdr_details import Mdr_details
from .measurement_unit import Measurement_unit
from .mr_item import MrItem
from .partner import Partner


from .permission import Permission

from .position import Position


from .project_demand import Project_demand

from .project_demand_details import Project_demand_details

from .refresh_token import RefreshToken
from .second_phase import Second_Phase
from .tender_extra_cost import Tender_Extra_Cost


# from .statement import Statement

# from .statement_items import Statement_items

from .user_position import User_position
from .user import User

# Workflow engine models
from .wf_template import WfTemplate
from .wf_step import WfStep
from .wf_step_actor import WfStepActor
from .wf_instance import WfInstance
from .wf_task import WfTask
from .wf_action_log import WfActionLog

# Payment models
from .commercial_payment import CommercialPayment
from .payment_condition import Payment_Condition


class Base(AsyncAttrs, DeclarativeBase):
    pass


__all__ = [
    "Base",
    "Activity_type",
    # "Addendum",
    "Bank_Account",
    "Bank",
    "Bidder_list",
    # "Bidder",
    # "Bidders_Document",
    "Cbs_element",
    # "Cbs_element_history",
    "Cbs_type",
    "Contract",
    "Contract_Item",
    # "Contract_item_history",
    "Currency",
    "Delivery_type",
    "Demand",
    "Demand_document",
    "Demand_document_type",
    "Department",
    "Employee",
    "Extra_Cost",
    "Form_Entity",
    # "Inquery",
    "Main_addendum",
    "Main_phase",
    "Main_project",
    "Mdr_details",
    "Mdr",
    "Measurement_unit",
    "MrItem",
    "Partner",
    "Permission",
    "Position",
    "Project_demand",
    "Project_demand_details",
    "RefreshToken",
    "Second_Phase",
    "Tender_Extra_Cost",
    # "Statement",
    # "Statement_items",
    "User_position",
    "User",
    "WfTemplate",
    "WfStep",
    "WfStepActor",
    "WfInstance",
    "WfTask",
    "WfActionLog",
    "CommercialPayment",
    "Payment_Condition",
]
