import os
import init
import pandas as pd

df_all = []
df_grouped = []

for root, dirs, files in os.walk(init.directory_path):
    for file in files:
        print(os.path.join(root, file))
        df = pd.read_csv(os.path.join(root, file))
        df = df[df[init.date]>=init.start_day]
        df1 = df.groupby(init.date)[[init.open,]].mean()
        df1.columns = [df[init.ticker_col].iat[0]]
        df1.columns = df1.columns.str.replace("RMFS4 [TQOB]","")
        df1.columns = df1.columns.str.replace("RMFS9 [TQOB]", "")
        df1.columns = df1.columns.str.replace("SU", "")
        df1.columns = df1.columns.str.replace("RMFS3 [TQOB]", "")
        df_all.append(df)
        df_grouped.append(df1)
        print(df[init.ticker_col].iat[0], df[init.date].iat[0],
              df[init.date].iat[-1])

for i in df_grouped:
    print(i.count())
