from convert_models.cbs_element import Cbs_element
from convert_models.main_project import Main_project
from convert_models.pre_contract import Pre_contract
from convert_models.contract_item import Contract_item
import functions as func





def convert(inp_val:list)->list:
    precontract_id_map = func.convert_id(Pre_contract)
    cbs_element_id_map = func.convert_id(Cbs_element)
    results = []
    for row in inp_val:
        element = Contract_item(
            contract_id = precontract_id_map.get(row['CtorContractNo']),
            cbs_element_id = cbs_element_id_map.get(row['ElementNo']),
            local_amount = row['PaymentLocal'],
            foreign_amout = row['PaymentForeign'],
            register_date = func.shamsi_to_miladi(str(row['RegDate']).strip()),
        )
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from ContratorCbsItems')
    new_data = convert(old_data)
    # rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')