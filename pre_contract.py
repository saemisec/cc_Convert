import enum
from models.partner import Partner
from models.currency import Currency
from models.main_project import Main_project
import functions as func
from models.contract import Contract
from models.delivery_type import Delivery_type

import functions as func

class Contract_status(enum.Enum):
    INPROGRESS = "InProgress"
    CANCELED = "Canceled"
    TOCONTRACT = "ToContract"





def convert(inp_val:list)->list:
    results = []
    delivery_type_id_map = func.convert_id(Delivery_type)
    # precontract_id_map = func.convert_id(Pre_contract)
    bank_account_id_map = func.get_bank_account_list()
    partner_id_map = func.convert_id(Partner)
    currency_id_map = func.convert_id(Currency)
    secondphase_id_map = func.convert_sec_phase()
    prj_id_map = func.convert_prj_phase()
    for row in inp_val:
        req_num = str(row['RequestNum']).strip().split('_')
        main_phase_id = func.convert_main_phase(str(req_num[1]).strip())
        #print(main_phase_id)
        if main_phase_id is None:
            print('None')
            breakpoint()
        if main_phase_id<1 or main_phase_id>8 :
            breakpoint()
        element = Contract(
            old_id = row['RequestNo'],
            title = str(row['RequestSubject']).strip(),
            partner_id = partner_id_map.get(row['ContractorNo']),
            main_project_id = prj_id_map.get(str(req_num[0]).strip()),
            number= str(row['RequestNum']).strip(),
            request_number = str(row['AdoptNum']).strip(),
            amount_irr = row['RoughSumLocal'],
            amount_cur = row['RoughSumForeign'],
            register_date = func.shamsi_to_miladi(str(row['RequestDate']).strip()),
            # register_duration = row['Deadline'],
            contract_status = "INPROGRESS",
            currency_id = currency_id_map.get(row['CurrencyCode']) if row['RoughSumForeign']>0 else None,
            main_phase_id = func.convert_main_phase(str(req_num[1]).strip()),
            second_phase_id = secondphase_id_map.get(str(req_num[2]).strip()),
            bank_account_id = [x['bank_account_id'] for x in bank_account_id_map if x['Bank_old_id']==row['BankNo'] and x['account_number']==str(row['AccountNo']).strip()][0],
            insu_percent = row['InsuRate'] ,
            tax_percent = row['TaxRate'] ,
            good_job_percent = row['ExcelOfPerform'],
            is_vat_contain = row['HasVAT'],
            prepayment_irr = row['DownPayLocal'],
            prepayment_cur = row['DownPayForeign'],
            prepayment_percent = row['Depreciation'],
            delivery_type_id = delivery_type_id_map.get(row['GoodDeliverNo']),
            registration_date = func.shamsi_to_miladi(str(row['RegDate']).strip()),
            fine_percent = row['GoodDeliverPenalty'],
            delivery_type_desc = str(row['GoodDeliverPenaltyDes']).strip(),
            # contract_rate = 'CONST_RATE' if row['PriceType'] == 1 else 'ATTACH_RATE',
            contractor_obligations = str(row['CtorUndertake']).strip(),
            employer_obligations = str(row['EmplrUndertake']).strip(),
            start_date = func.shamsi_to_miladi(str(row['StartDate']).strip()),
            desc = str(row['ContractDes']).strip(),
            duration = row['TimeFrame']
        )
        results.append(element)
    return results

def merge_lists_by_key(list1, list2, key1, key2):
    map2 = {item[key2]: item for item in list2}
    merged = []
    for item1 in list1:
        key_val = item1[key1]
        if key_val in map2:
            merged_item = {**item1, **map2[key_val]}
            merged.append(merged_item)
    return merged

if __name__ == "__main__":
    old_data_request_num = func.get_old_data('select * from ContractorRequestNum')
    old_data_contractor = func.get_old_data('select * from ContractorContracts')
    merged_data = merge_lists_by_key(old_data_request_num, old_data_contractor, 'RequestNo', 'CtorContractNo')
    new_data = convert(merged_data)
    rr = func.model_list(new_data)
    # breakpoint()
    func.insert_new_record(new_data)
    print('Well done.')

