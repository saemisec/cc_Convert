from convert_models.bank_account import Bank_Account
from convert_models.partner import Partner
from convert_models.bank import Bank
import functions as func


def convert(inp_val:list)->list:
    results = []
    bank_id_map = func.convert_id(Bank)
    partner_id_map = func.convert_id(Partner)
    for row in inp_val:
        element = Bank_Account(
            account_number = str(row['AccountNo']).strip(),
            bank_id = bank_id_map.get(row['BankNo']),
            parter_id = partner_id_map.get(row['ContractorNo']),
            is_default = False,
            desc = str(row['AccDes']).strip())
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from ContractorAccNums')
    new_data = convert(old_data)
    func.insert_new_record(new_data)
    print('Well done.')