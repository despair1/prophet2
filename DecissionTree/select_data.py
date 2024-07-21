import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def select_data(df_open_merged: pd.DataFrame, target: int):
    df = df_open_merged
    df["y"] = df.iloc[:, 0].shift(-3)
    y = df.y[:-3]
    X = df.iloc[:-3,[i for i in range(df.shape[1]-1)]]
    print(y.tail())
    print(X.tail())
    model = DecisionTreeRegressor()
    model.fit(X,y)
    print(X.tail(10))
    print(df_open_merged.tail(10))
    print(model.predict(X.tail(10)))



    X1 = df_open_merged.drop("y",axis=1)
    print(model.predict(X1.tail(10)))

