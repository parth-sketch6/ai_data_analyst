import sqlite3
import pandas as pd


def register_dataframe(df, table_name="data"):
    connection = sqlite3.connect(":memory:")

    df.to_sql(
        table_name,
        connection,
        index=False,
        if_exists="replace"
    )

    return connection


def execute_query(connection, query):
    try:
        result = pd.read_sql_query(query, connection)

        return {
            "success": True,
            "data": result,
            "error": None
        }

    except Exception as e:
        return {
            "success": False,
            "data": None,
            "error": str(e)
        }