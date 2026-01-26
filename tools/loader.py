import pandas as pd

def load_data(csv_path: str):
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"])
    return {
        "rows": len(df),
        "columns": list(df.columns)
    }
