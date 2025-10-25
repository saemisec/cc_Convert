import enum
from convert_models.pre_contract import Pre_contract
from convert_models.partner import Partner
from convert_models.currency import Currency
from convert_models.main_project import Main_project
import functions as func

class Contract_status(enum.Enum):
    INPROGRESS = "InProgress"
    CANCELED = "Canceled"
    TOCONTRACT = "ToContract"

def convert(inp_val:list)->list:
    results = []
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
        element = Pre_contract(
            old_id = row['RequestNo'],
            title = str(row['RequestSubject']).strip(),
            partner_id = partner_id_map.get(row['ContractorNo']),
            main_project_id = prj_id_map.get(str(req_num[0]).strip()),
            number= str(row['RequestNum']).strip(),
            request_number = str(row['AdoptNum']).strip(),
            amount_irr = row['RoughSumLocal'],
            amount_cur = row['RoughSumForeign'],
            register_date = func.shamsi_to_miladi(str(row['RequestDate']).strip()),
            register_duration = row['Deadline'],
            contract_status = "INPROGRESS",
            currency_id = currency_id_map.get(row['CurrencyCode']) if row['RoughSumForeign']>0 else None,
            main_phase_id = func.convert_main_phase(str(req_num[1]).strip()),
            second_phase_id = secondphase_id_map.get(str(req_num[2]).strip()),
        )
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from ContractorRequestNum')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')

