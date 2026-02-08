from functions import insert_new_record,get_old_data
from models.extra_cost import Extra_Cost


def extra_cost_convert(inp_val:list):
    ExtraCosts = []
    seen_names = set()
    for row in inp_val:
        name = str(row['ExpenseTitle']).strip()
        if name not in seen_names:
            extra_cost = Extra_Cost(old_id = row['ExpenseNo'],
                        name = name)
            ExtraCosts.append(extra_cost)
            seen_names.add(name)
    return ExtraCosts  
    
if __name__ == "__main__":
    old_data = get_old_data('select * from CtorCtExpenseItemsDef')
    new_data = extra_cost_convert(old_data)
    

    insert_new_record(new_data)
    print('Well done.')