from models.partner import Partner
import functions as func

def convert_person(inp_val:list)->list:
    results = []
    for row in inp_val:
        element = Partner(
            old_id = row['PersonNo'],
            full_name = str(row['LName']).strip() + ' - ' + str(row['FName']).strip(),
            national_id = str(row['NationalNo']).strip(),
            economic_code = None,
            is_legal_entity = False,
            address = str(row['Address']).strip(),
            is_vendor = row['Seller'],
            is_contructor = row['Contractor'])
        results.append(element)
    return results

def convert_company(inp_val:list)->list:
    results = []
    for row in inp_val:
        element = Partner(
            old_id = row['CompanyNo'],
            full_name = str(row['CompanyName']).strip(),
            national_id = str(row['NationalId']).strip(),
            economic_code = str(row['EconomyNum']).strip(),
            is_legal_entity = True,
            address = str(row['Address']).strip(),
            is_vendor = row['Seller'],
            is_contructor = row['Contractor'])
        results.append(element)
    return results



if __name__ == "__main__":
    old_data = func.get_old_data('select * from Persons')
    new_data = convert_person(old_data)
    old_data = func.get_old_data('select * from Companies')
    new_data.extend(convert_company(old_data))
    rr = func.model_list(new_data)
    func.insert_new_record(new_data)
    print('Well done.')