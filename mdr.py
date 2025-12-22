from models.mdr import Mdr
from functions import fetch_cbs_data, insert_new_record, fetch_mdr_data, model_list, svc_parse_item_excel


def get_cbs_id(document_no: str, excel_data: list,cbs_data) -> int:
    wbs_code = [x for x in excel_data if str(x["document_no"]).strip() == str(document_no).strip()]
    if wbs_code is None or len(wbs_code) == 0:
        print(f"No WBS code found for Document No: {document_no}")
        return None
    wbs_code = wbs_code[0]["wbs_code"]
    print(f"Document No: {document_no} maps to WBS Code: {wbs_code}")
    cbs_id = [x for x in cbs_data if x.wbs_code == wbs_code]
    if cbs_id is None or len(cbs_id) == 0:
        print(f"No CBS ID found for WBS code: {wbs_code}")
        return None
    cbs_id = cbs_id[0].id
    print(f"WBS Code: {wbs_code} maps to CBS ID: {cbs_id}")
    if cbs_id is None :
        print(f"No CBS ID found for WBS code: {wbs_code}")
        return None
    return cbs_id

def convert(inp_val: list) -> list:
    results = []
    cbs_data = fetch_cbs_data()
    excel_data = svc_parse_item_excel()
    for row in inp_val:
        element = Mdr(
            main_project_id=12,
            document_no=str(row.document_no).strip(),
            cbs_element_id = get_cbs_id(row.document_no,excel_data,cbs_data,),
            title=str(row.title).strip(),
            type=str(row.type).strip(),
            last_rev=str(row.last_rev).strip(),
            discipline=(row.discipline).strip(),
        )
        results.append(element)

    return results


if __name__ == "__main__":
    old_data = fetch_mdr_data()
    new_data = convert(old_data)
    rr = model_list(new_data)
    # breakpoint()
    insert_new_record(new_data)
    print("Well done.")
