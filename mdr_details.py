from functions import insert_new_record, model_list, fetch_mdr_details_data
from models.mdr_details import Mdr_details




def convert(inp_val: list) -> list:
    results = []
    for row in inp_val:
        element = Mdr_details(
            mdr_id=row.mdr_id,
            rev=row.rev,
            receipt_date=row.receipt_date,
            disk_id=row.disk_id,
            files=row.files,
        )
        results.append(element)
    return results

if __name__ == "__main__":
    old_data = fetch_mdr_details_data()
    new_data = convert(old_data)
    rr = model_list(new_data)
    # breakpoint()
    insert_new_record(new_data)
    print("Well done.")