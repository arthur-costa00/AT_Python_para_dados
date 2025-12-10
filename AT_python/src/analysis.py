import pandas as pd

def criar_dataframe(lista):
    return pd.DataFrame(lista)

def top_n(df, n):
    return df.sort_values("nota", ascending=False).head(n)

def media_notas(df):
    return df["nota"].mean()
