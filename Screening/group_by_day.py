import init
import pandas as pd
from typing import List

def group_by_day(dfs: List[pd.DataFrame])->List[pd.DataFrame]:
    dfa = []
    for i in dfs:
        df = i.groupby(init.date)[[init.open,]].mean()
        df.columns = [i[init.ticker_col].iat[0]]
        dfa.append(df)
    return dfa
