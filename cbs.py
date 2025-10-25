from convert_models.cbs import Cbs
from convert_models.main_project import Main_project

import functions as func


def convert(inp_val:list)->list:
    results = []
    main_project_id_map = func.convert_id(Main_project)
    for row in inp_val:
        element = Cbs(
            old_id = row['ElementNo'],
            title = str(row['ElementTitle']).strip(),
            code = row['ElementNum'],
            amount_irr = row['ElPaymentLocal'],
            amount_cur = row['ElPaymentForeign'],
            main_project_id = main_project_id_map.get(row['ContractElNo']),
            type = row['ElementType'])
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from CElements')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')