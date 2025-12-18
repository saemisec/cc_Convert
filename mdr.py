from models.mdr import Mdr
from functions import insert_new_record, fetch_mdr_data


def convert(inp_val: list) -> list:
    results = []
    for row in inp_val:
        element = Mdr(
            main_project_id=12,
            document_no=str(row.document_no).strip(),
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
    insert_new_record(new_data)
    print("Well done.")
