from functions import insert_new_record,get_old_data
from models.second_phase import Second_Phase


def second_phase_convert(inp_val:list):
    SecondPhases = []
    for row in inp_val:
        second_phase = Second_Phase(old_id = row['ExtNo'],
                    name = str(row['ContractExt']).strip())
        SecondPhases.append(second_phase)
    return SecondPhases
    
if __name__ == "__main__":
    old_data = get_old_data('select * from ContractorCntrExt')
    new_data = second_phase_convert(old_data)
    insert_new_record(new_data)
    print('Well done.')