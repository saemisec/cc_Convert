
from  convert_models.employee import Employee
from functions import insert_new_record,get_old_data

def employee_convert(inp_val:list)->list:
    results = []
    
    for row in inp_val:
        element = Employee(old_id = row['EmplrNo'],
                    name = str(row['EmplrTitle']).strip())
        results.append(element)
    
    return results

if __name__ == "__main__":
    old_data = get_old_data('select * from Employers')
    new_data = employee_convert(old_data)
    insert_new_record(new_data)
    print('Well done.')