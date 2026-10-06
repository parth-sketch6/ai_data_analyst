import pandas as pd


def detect_semantic_type(df, column):

    if column.lower().endswith("_id") or column.lower() == "id":
        return "identifier"

    elif pd.api.types.is_datetime64_any_dtype(df[column]):
        return "datetime"

    elif pd.api.types.is_numeric_dtype(df[column]):
        return "numeric"

    else:
        return "categorical"


def profile_data(df):

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_info": {}
    }

    for column in df.columns:

        semantic_type = detect_semantic_type(df, column)

        column_info = {
            "dtype": str(df[column].dtype),
            "semantic_type": semantic_type,
            "missing_values": int(df[column].isnull().sum()),
            "unique_values": int(df[column].nunique())
        }

        if semantic_type == "numeric":

            column_info["statistics"] = {
                "min": df[column].min(),
                "max": df[column].max(),
                "mean": df[column].mean(),
                "median": df[column].median()
            }

        elif semantic_type == "categorical":

            column_info["values"] = (
                df[column]
                .dropna()
                .unique()
                .tolist()
            )

        profile["column_info"][column] = column_info

    return profile