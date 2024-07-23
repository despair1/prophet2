import pandas as pd


def val_list2index_list(df: pd.DataFrame, col_ind, start_val, end_val):
    col_name = df.columns[col_ind]
    filtered_indices = df[
        (df[col_name] >= start_val) & (df[col_name] <= end_val)].index
    print(filtered_indices)