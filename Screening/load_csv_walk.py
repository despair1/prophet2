import os
import init
import pandas as pd
from typing import List


def load_csv_walk(path = init.directory_path, start_day = init.start_day)\
        -> List[pd.DataFrame]:
    df_all = []
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
            df = pd.read_csv(os.path.join(root, file))
            df = df[df[init.date] >= start_day]
            df_all.append(df)
    return df_all