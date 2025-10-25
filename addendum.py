from convert_models.pre_contract import Pre_contract
from convert_models.addendum import Addendum
import functions as func


def convert(inp_val:list)->list:
    results = []
    Pre_contract_id_map = func.convert_id(Pre_contract)
    for row in inp_val:
        element = Addendum(
            old_id = row['MoneyRevNo'],
            pre_contract_id = Pre_contract_id_map.get(row['CtorContractNo']),
            title = '',
            rev_no = 1,
            revdate = func.shamsi_to_miladi(str(row['RevDate']).strip()),
            revdesc = str(row['RevDes']).strip(),
            amount_extend_irr = row['RevPayLocal'],
            amount_extend_cur = row['RevPayForeign'],
            date_extend = 0,
            RegDate = func.shamsi_to_miladi(str(row['RegDate']).strip()))
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from CtorCtMoneyRev ')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    #breakpoint()
    func.insert_new_record(new_data)
    print('Well done.')