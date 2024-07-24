from day_mean_all_ofz import day_mean_all
import pandas as pd


df = day_mean_all()
df = df.resample("ME").mean()
df.columns = [col[:5] for col in df.columns]
print(df)
# print(range(df.shape[1]))
for i in range(df.shape[1]):
    df["y"] = df.iloc[:,i].shift(-1)
    c = df.columns[i]
    df[c] = df["y"]/df[c]
    df[c] = (df[c]**12-1)*100
del df["y"]
print(df)