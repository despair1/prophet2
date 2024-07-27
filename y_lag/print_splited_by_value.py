import init
from get_dict_tmstmp_by_val import get_dict_tmstmp_by_val
from load_csv_by_key import load_csv_by_key
import pandas as pd
from splited_by_value_report import splited_by_value_report
from group_by_day_report import group_by_day_report

dict = get_dict_tmstmp_by_val()
for k,v in dict.items():
    print(k,v)
    df = load_csv_by_key(k)
    pd.options.display.float_format = '{:.2f}'.format
    df2 = group_by_day_report(df)
    df2.index = pd.to_datetime(df2.index, format='%Y%m%d')
    print(df2)
    # df["day"] = pd.to_datetime(df[init.date], format='%Y%m%d')
    # df.set_index("day", inplace=True)
    df1 = splited_by_value_report(df2,v)

    df1["decr"] = df1[init.e_col]/df1[init.b_col]/df1[init.count_col]*100
    print(df1)
    # print(df.tail(15))
    # print(df_dict)
    # print(df.dtypes)




