import init
from get_dict_tmstmp_by_val import get_dict_tmstmp_by_val
from load_csv_by_key import load_csv_by_key
import pandas as pd

dict = get_dict_tmstmp_by_val()
for k,v in dict.items():
    print(k,v)
    df = load_csv_by_key(k)
    pd.options.display.float_format = '{:.2f}'.format
    st = v[0]
    tmst = v[1:]
    df["day"] = pd.to_datetime(df[init.date], format='%Y%m%d')
    df.set_index("day", inplace=True)
    df_dict = { init.date : [], init.count_col : [],
                init.low_col : [], init.mean_col : [],
                init.high_col : [],
                init.b_col : [], init.e_col: []}
    for i in tmst:
        # print(df[st:i].describe())
        df1 = df[st:i]
        df_dict[init.date].append(df1.index[0])
        df_dict[init.count_col].append(df1[init.date].count())
        df_dict[init.mean_col].append(df1[init.open].mean())
        df_dict[init.low_col].append(df1[init.low_col].quantile(init.qlow))
        df_dict[init.high_col].append(df1[init.high_col].quantile(init.qhigh))
        df_dict[init.b_col].append(df1[init.open].iloc[0:init.begin].mean())
        df_dict[init.e_col].append(df1[init.open].iloc[init.end:].mean())
        st=i
    df1 = pd.DataFrame(df_dict)
    df1["decr"] = df1[init.e_col]/df1[init.b_col]/df1[init.count_col]*100
    print(df1)
    # print(df.tail(15))
    # print(df_dict)
    # print(df.dtypes)




