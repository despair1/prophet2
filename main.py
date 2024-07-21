import os
from prophet import  Prophet
import init
import pandas as pd

for dirname, _, filenames in os.walk(r"C:\alina\ofz"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

pd.set_option("display.max_columns", None)
path = r"C:\alina\ofz\ОФЗ 26243 [Price].txt"
df = pd.read_csv(path)
print(df.tail())
print(df.dtypes)
df = df[[init.date,init.open]]
df.columns = ["ds","y"]
df["ds"] = pd.to_datetime(df['ds'], format='%Y%m%d')
print(df.tail(20))
#dffdf
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(10)
guess = model.predict(future)
print(guess.tail(20))
model.plot(guess)