from models.pre_contract import Pre_contract
from models.statement import Statement
import functions as func





def convert(inp_val:list)->list:
    precontract_id_map = func.convert_id(Pre_contract)
    results = []
    for row in inp_val:
        element = Statement(
            old_id = row['InvoiceNo'],
            contract_id = precontract_id_map.get(row['CtorContractNo']),
            amount_irr = row['InvPriceLocal'],
            amount_cur = row['InvPriceForeign'],
            number = row['InvoiceNum'],
            statement_date = func.shamsi_to_miladi(str(row['InvDate']).strip()),
            register_date = func.shamsi_to_miladi(str(row['RegDate']).strip()),
        )
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from CtorCtInvoice')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    # breakpoint()
    func.insert_new_record(new_data)
    print('Well done.')