from convert_models.payment_condition import Payment_condition
from convert_models.pre_contract import Pre_contract
import functions as func



def convert(inp_val:list)->list:
    results = []
    contract_id_map = func.convert_id(Pre_contract)
    for row in inp_val:
        element = Payment_condition(
            contract_id = contract_id_map.get(row['CtorContractNo']),
            desc = str(row['CondTitle']).strip(),
            value = row['CondPercent'],
        )
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from PaymentConds')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')