from models.measurement_unit import Measurement_unit
import functions as func


def convert(inp_val:list)->list:
    results = []
    for row in inp_val:
        element = Measurement_unit(
            old_id = row['UnitNo'],
            name = str(row['UnitTitle']).strip(),
            is_nemeric = True if row['IsInt']==1 else False,
            code = str(row['UnitCode']).strip()
        )
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from PartUnits')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')