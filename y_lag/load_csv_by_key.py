import os
import init
import pandas as pd
from typing import List


def load_csv_by_key(key, path = init.directory_path)\
        -> pd.DataFrame:
    for root, dirs, files in os.walk(path):
        for file in files:
            if key not in file: continue
            print(file)
            # print(os.path.join(root, file))
            df = pd.read_csv(os.path.join(root, file))
            return df
            df = df[df[init.date] >= start_day]
            df_all.append(df)
    return