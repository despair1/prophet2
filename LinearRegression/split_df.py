import pandas as pd
import init

def split_df(df: pd.DataFrame):
    #start, end = df[init.date_column].iloc[[0, -1]]
    # size = (end - start)/ init.split
    # print(size)
    sample_size = len(df) // init.split + 1
    sample_arr = []
    for i in range(0, len(df), sample_size):
        sample_arr.append(df[i:i+sample_size])
    # print(sample_arr)
    return sample_arr