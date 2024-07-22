import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def select_data(df_open_merged: pd.DataFrame, target: int):
    df = df_open_merged
    df["y"] = df.iloc[:, 0].shift(-1)
    y = df.y[:-5]
    X = df.iloc[:-5,[i for i in range(df.shape[1]-1)]]
    X1 = df.iloc[-10:, [i for i in range(df.shape[1] - 1)]]
    #print(y.tail())
    #print(X.tail())
    model = DecisionTreeRegressor()
    model.fit(X,y)
    #print(X.tail(10))
    #print(df_open_merged.tail(10))
    print(X1)
    print(model.predict(X1))



