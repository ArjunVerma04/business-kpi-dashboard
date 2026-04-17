import pandas as pd
import sqlite3

def create_db():
    conn = sqlite3.connect("sales.db")
    df = pd.read_csv("data/sales_data.csv")
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()

def get_connection():
    return sqlite3.connect("sales.db")