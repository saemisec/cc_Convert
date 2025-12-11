from models.contract import Contract
from models.delivery_type import Delivery_type
from models.pre_contract import Pre_contract
import functions as func

def convert(inp_val:list)->list:
    results = []
    delivery_type_id_map = func.convert_id(Delivery_type)
    precontract_id_map = func.convert_id(Pre_contract)
    bank_account_id_map = func.get_bank_account_list()
    for row in inp_val:
        element = Contract(
            id = precontract_id_map.get(row['CtorContractNo']),
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
            contract_rate = 'CONST_RATE' if row['PriceType'] == 1 else 'ATTACH_RATE',
            contractor_obligations = str(row['CtorUndertake']).strip(),
            employer_obligations = str(row['EmplrUndertake']).strip(),
            start_date = func.shamsi_to_miladi(str(row['StartDate']).strip()),
            desc = str(row['ContractDes']).strip(),
            duration = row['TimeFrame'])
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from ContractorContracts')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')
