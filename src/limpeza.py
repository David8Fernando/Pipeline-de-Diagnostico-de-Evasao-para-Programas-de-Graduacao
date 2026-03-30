import pandas as pd
def limpar_dados(df):
    df = df.drop_duplicates()

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df