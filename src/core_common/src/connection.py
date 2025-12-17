import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine

load_dotenv("/Desktop/dev.env")

ODBC_DRIVER = "ODBC Driver 17"
DATABASE_SERVER = str(os.getenv("server"))
DATABASE_NAME = str(os.getenv("database"))
DATABASE_USER = str(os.getenv("uid"))
DATABASE_PWD = str(os.getenv("pwd"))

odbc_str = f'DRIVER={ODBC_DRIVER};SERVER={DATABASE_SERVER};PORT=1443;DATABASE={DATABASE_NAME};UID={DATABASE_USER};PWD={DATABASE_PWD}'
connect_str = f'mssql+pyodbc:///?odbc_connect={odbc_str}'

engine = create_engine(connect_str)
