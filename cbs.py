from convert_models.cbs_element import Cbs_element
from convert_models.main_project import Main_project

import functions as func


def convert(inp_val:list)->list:
    results = []
    for row in inp_val:
        element = Cbs_element(
            old_id = row['ElementNo'],
            title = str(row['ElementTitle']).strip(),
            code = row['ElementNum'],
            local_amount = row['ElPaymentLocal'],
            foreign_amout = row['ElPaymentForeign'],
            main_project_id = func.convert_prj_id_cbs(row['ContractElNo']),
            element_type = 8  if row['ElementType']==9 else row['ElementType'],
            rev_no = row['RevNo'])
            #parent_id = [x[] for x in inp_val    func.get_parent_id(row['ElementNum']))
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from CElements')
    new_data = convert(old_data)
    # rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')