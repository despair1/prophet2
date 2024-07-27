import pandas as pd
import init

def group_by_day_report(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(init.date).agg({
        init.open: "mean",
        init.low_col: "min",
        init.high_col: "max"
    })
    return df
        #[[init.open, ]].mean()