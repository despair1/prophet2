import os
import init
import pandas as pd

df_all = []

for root, dirs, files in os.walk(init.directory_path):
    for file in files:
        print(os.path.join(root, file))
        df = pd.read_csv(os.path.join(root, file))
        df = df[df[init.date]>=init.start_day]
        df = df.groupby(init.date)[[init.open,]].mean()
        df_all.append(df)
for i in df_all:
    print(i.count())
