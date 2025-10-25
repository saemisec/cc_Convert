from functions import insert_new_record,get_old_data
from convert_models.bank import Bank


def bank_convert(inp_val:list):
    Banks = []
    for row in inp_val:
        bank = Bank(old_id = row['BankNo'],
                    name = str(row['BankName']).strip())
        Banks.append(bank)
    return Banks
    
if __name__ == "__main__":
    old_data = get_old_data('select * from Banks')
    new_data = bank_convert(old_data)
    insert_new_record(new_data)
    print('Well done.')