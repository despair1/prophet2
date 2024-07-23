import init
import load_files as lf
from merge_open import merge_open
df = merge_open(lf.df_grouped)
import matplotlib.pyplot as plt
import pandas as pd
from split_df import split_df

df.info()
df_spl = split_df(df)
for df in df_spl:
    s1 = pd.Series(df.mean(), name=init.mean_col)
    s2 = pd.Series(df.var(), name=init.var_col)
    # print(df.mean())
    # print(df.var())
    df1 = pd.concat([s1,s2],axis=1)
    print(df1)