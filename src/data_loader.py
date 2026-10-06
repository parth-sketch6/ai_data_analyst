import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)

    for column in df.columns:
        if "date" in column.lower():
            df[column] = pd.to_datetime(df[column], errors="coerce")

    return df