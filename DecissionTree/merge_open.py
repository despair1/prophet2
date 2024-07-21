import pandas as pd
from typing import List



def merge_open(dfs : List[pd.DataFrame]) -> pd.DataFrame:
    df_open = None
    for i,v in enumerate(dfs):
        if not i:
            df_open = v
            continue
        df_open = df_open.merge(v,left_index=True, right_index=True)
    return df_open

