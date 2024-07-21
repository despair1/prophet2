import pandas as pd
from sklearn.tree import DecisionTreeRegressor

def select_data1(df_open_merged: pd.DataFrame, tail: int, target: int):
    df = df_open_merged
    y = df.iloc[:-tail, target]
    X = df.drop(df.columns[target], axis=1)
    X = X[:-tail]
    #print(y.tail())
    #print(X.tail())
    print(df.tail(tail))
    model = DecisionTreeRegressor()
    model.fit(X,y)
    X1 = df.drop(df.columns[target], axis=1)
    print(model.predict(X1.tail(tail)))


