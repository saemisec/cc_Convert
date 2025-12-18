import os
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker, Session
from typing import Type, Dict
import pyodbc
import re
from persiantools.jdatetime import JalaliDate
import datetime
import csv
from models.second_phase import Second_Phase
from models.main_project import Main_project
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
NEW_DATABASE_URL = os.getenv("NEW_DATABASE_URL")


def get_id_map(
    session: Session,
    model: Type,
    old_id_field_name: str = "old_id",
    new_id_field_name: str = "id",
) -> Dict[int, int]:
    old_id_attr = getattr(model, old_id_field_name)
    new_id_attr = getattr(model, new_id_field_name)

    result = session.execute(select(old_id_attr, new_id_attr)).all()
    return {old: new for old, new in result}


def get_bank_account_list():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    sql = text(
        """
    select ba.account_number as account_number ,b.old_id as Bank_old_id ,ba.id as bank_account_id
    from bank_account ba
    inner join bank b on b.id = ba.bank_id 
    """
    )
    query_results = session.execute(sql).fetchall()
    results = []
    for row in query_results:
        results.append(
            {"account_number": row[0], "Bank_old_id": row[1], "bank_account_id": row[2]}
        )
    # lookup = [(row[0], row[1]): row[2] for row in results]
    return results


def clean_invisible_chars(text: str) -> str:
    return re.sub(r"[\u200b\u200c\u200d\u200e\u200f]+", "", text)


def get_old_data(query: str) -> list:
    results = []
    server = os.getenv("SQL_ADDRESS")
    database = os.getenv("SQL_DB")
    username = os.getenv("SA_USER")
    password = os.getenv("SA_PASSWORD")
    conn_str = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"TrustServerCertificate=yes;"
        f"PWD={password}"
    )
    cleaned_data = []
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            cleaned_row = {
                col: clean_invisible_chars(str(val)) if isinstance(val, str) else val
                for col, val in zip(columns, row)
            }
            cleaned_data.append(cleaned_row)
            row_dict = dict(zip(columns, row))
            results.append(row_dict)
    except Exception as e:
        print("Error in connection:", e)
    return cleaned_data


def postgres_session() -> sessionmaker:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    return session


def fetch_mdr_data() -> list:
    sql = text(
        """
    SELECT document_no ,title ,discipline ,last_rev,type 
    FROM edms_mdr where project_id = 6 and document_no like '1389-AR-%'
    """
    )

    engine = create_engine(NEW_DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    results = session.execute(sql).fetchall()
    return results


def insert_new_record(inp_val: list):
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    session.bulk_save_objects(inp_val)
    session.commit()


def convert_prj_id_cbs(inp_val: int):
    if inp_val == 7:
        return 1
    elif inp_val == 8:
        return 2
    elif inp_val == 12:
        return 3
    elif inp_val == 21:
        return 4
    elif inp_val == 13:
        return 5
    elif inp_val == 15:
        return 6
    elif inp_val == 26:
        return 8
    elif inp_val == 28:
        return 9
    elif inp_val == 19:
        return 10
    elif inp_val == 20:
        return 11
    elif inp_val == 22:
        return 12
    elif inp_val == 23:
        return 13
    elif inp_val == 24:
        return 14
    elif inp_val == 25:
        return 15
    elif inp_val == 27:
        return 16
    elif inp_val == 29:
        return 17
    elif inp_val == 30:
        return 18


def convert_prj_id_mdr(inp_val: int):
    if inp_val == 6:
        return 12
    elif inp_val == 8:
        return 2
    elif inp_val == 12:
        return 3
    elif inp_val == 21:
        return 4
    elif inp_val == 13:
        return 5
    elif inp_val == 15:
        return 6
    elif inp_val == 26:
        return 8
    elif inp_val == 28:
        return 9
    elif inp_val == 19:
        return 10
    elif inp_val == 20:
        return 11
    elif inp_val == 22:
        return 12
    elif inp_val == 23:
        return 13
    elif inp_val == 24:
        return 14
    elif inp_val == 25:
        return 15
    elif inp_val == 27:
        return 16
    elif inp_val == 29:
        return 17
    elif inp_val == 30:
        return 18


def convert_id(parent_table: str) -> list:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    return get_id_map(
        session, parent_table, old_id_field_name="old_id", new_id_field_name="id"
    )


def convert_sec_phase() -> list:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    return get_id_map(
        session, Second_Phase, old_id_field_name="name", new_id_field_name="id"
    )


def convert_prj_phase() -> list:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    return get_id_map(
        session, Main_project, old_id_field_name="Abbreviation", new_id_field_name="id"
    )


def model_to_dict(instance):
    return {
        column.name: getattr(instance, column.name)
        for column in instance.__table__.columns
    }


def model_list(lst: list):
    results = []
    for x in lst:
        results.append(model_to_dict(x))
    return results


def shamsi_to_miladi(inp_val: str):
    inp_val = inp_val.split("/")
    return JalaliDate(int(inp_val[0]), int(inp_val[1]), int(inp_val[2])).to_gregorian()


def convert_main_phase(inp_val: str) -> int:
    if inp_val.upper() == "E":
        return 1
    elif inp_val.upper() == "P":
        return 2
    elif inp_val.upper() == "C":
        return 3
    elif inp_val.upper() == "CO":
        return 4
    elif inp_val.upper() == "F":
        return 5
    elif inp_val.upper() == "MA":
        return 6
    elif inp_val.upper() == "MB":
        return 7


def get_parent_id(inp_val: str) -> str:
    if "." not in inp_val:
        return 0
    else:
        inp_array = inp_val.split(".")
        inp = inp_array[:-1]
        dest_str = ""
        for x in inp:
            dest_str = x + "." + dest_str
        if dest_str[len(dest_str) - 1] == ".":
            dest_str = dest_str[:-1]
        return dest_str


def get_project_type(*args):
    results = ""
    results = results + "E," if args[0] else results
    results = results + "P," if args[1] else results
    results = results + "C," if args[2] else results
    results = results + "CO," if args[3] else results
    results = results + "Ma," if args[4] else results
    results = results + "Mb," if args[5] else results
    results = results + "Dm," if args[6] else results
    if len(args) > 7:
        results = results + "F," if args[4] else results
    results = results[:-1]
    return results


def import_csv_to_db(csv_file_path: str):
    with open(csv_file_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
