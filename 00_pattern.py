from models.main_project import Main_project
from models.employee import Employee
from models.currency import Currency
import functions as func


def convert(inp_val:list)->list:
    results = []
    employee_id_map = func.convert_id(Employee)
    currency_id_map = func.convert_id(Currency)
    for row in inp_val:
        element = Main_project(
            #old_id = row['EmplrNo'],
            employee_id = employee_id_map.get(row['EmplrNo']),
            title = str(row['ContractTitle']).strip(),
            number = str(row['ContractNo']).strip(),
            Abbreviation = str(row['ContractAbr']).strip(),
            workshop_no = str(row['WorkshopNo']).strip(),
            agreement_number = str(row['WsContractNo']).strip(),
            amount_irr = row['GrossPaymentLocal'],
            amount_cur = row['GrossPaymentForeign'],
            currency_id = currency_id_map.get(row['CurrencyCode']),
            start_date = func.shamsi_to_miladi(str(row['StartDate']).strip()),
            insu_percent = row['InsuPercent'],
            tax_percent = row['TaxPercent'],
            insurance_policy = True if row['InsuPolicy']==2 else False,
            has_customs_duties = True if row['CustomDuty']==2 else False,
            customs_duties_desc = str(row['CustomDudyDes']).strip(),
            insurance_policy_desc = str(row['InsuPolicyDes']).strip(),
            adjustment_desc = str(row['ContractBaseMetric']).strip(),
            contruct_duration = row['TimeFrame'],
            good_job_percent = row['ExcelOfPerform'],
            contract_type = func.get_project_type(row['TypeE'],row['TypeP'],row['TypeC'],row['TypeCo'],row['TypeMa'],row['TypeMb'],row['TypeDm'],row['TypeF']),
            adjustment = func.get_project_type(row['AdjTypeE'],row['AdjTypeP'],row['AdjTypeC'],row['AdjTypeCo'],row['AdjTypeMa'],row['AdjTypeMb'],row['AdjTypeDm']),
            is_cost_center = False,
            contract_date = func.shamsi_to_miladi(str(row['ContactDate']).strip()),
            inform_date = func.shamsi_to_miladi(str(row['InformDate']).strip()),
            dl_date = func.shamsi_to_miladi(str(row['DlDate']).strip()))
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = func.get_old_data('select * from ')
    new_data = convert(old_data)
    rr = func.model_list(new_data)
    breakpoint()
    #func.insert_new_record(new_data)
    print('Well done.')