import pandas as pd


def sort_col_by_risen(df: pd.DataFrame):
    l = df.iloc[-1]/df.iloc[0]
    sorted_columns = l.sort_values(ascending=False).index
    sorted_df = df[sorted_columns]
    # l = l/ df.loc[0]
    print(l, sorted_columns)
    # print(sorted_df)
    return sorted_df