# src/database.py

import sqlite3


def create_connection(db_path="marketing.db"):
    conn = sqlite3.connect(db_path)
    return conn


def create_table(conn, df, table_name="campaign_data"):
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Table '{table_name}' created successfully.")


def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
