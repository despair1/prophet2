import pandas as pd
import init


def splited_by_value_report(df: pd.DataFrame, v) -> pd.DataFrame :
    st = v[0]
    tmst = v[1:]

    df_dict = { init.date : [], init.count_col : [],
                init.low_col : [], init.mean_col : [],
                init.high_col : [],
                init.b_col : [], init.e_col: []}
    for i in tmst:
        # print(df[st:i].describe())
        df1 = df[st:i]
        df_dict[init.date].append(df1.index[0])
        df_dict[init.count_col].append(df1[init.open].count())
        df_dict[init.mean_col].append(df1[init.open].mean())
        df_dict[init.low_col].append(df1[init.low_col].quantile(init.qlow))
        df_dict[init.high_col].append(df1[init.high_col].quantile(init.qhigh))
        df_dict[init.b_col].append(df1[init.open].iloc[0:init.begin].mean())
        df_dict[init.e_col].append(df1[init.open].iloc[init.end:].mean())
        st=i
        df1 = pd.DataFrame(df_dict)
    return df1