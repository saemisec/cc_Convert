from models.delivery_type import Delivery_type
from functions import insert_new_record,get_old_data

def convert(inp_val:list)->list:
    results = []
    for row in inp_val:
        element = Delivery_type(old_id = row['GoodDeliverNo'],
                    name = str(row['GoodDelivertTitle']).strip())
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = get_old_data('select * from GoodDeliveryKinds')
    new_data = convert(old_data)
    insert_new_record(new_data)