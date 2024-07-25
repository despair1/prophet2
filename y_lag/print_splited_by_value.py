import init
from day_mean_all_ofz import day_mean_all


df = day_mean_all()
for key,val in init.split_by_values.items():
    col = [col for col in df.columns if key  in col]
    if not col: continue
    print(col, val[0])
    # print(df[df[col]<val[0][col]].idxmin())
    # print(df[df[col] < val[0][col]].idxmax())
    col = col[0]
    # print(df.loc[-1:,col])
    print(df.loc[:,col].idxmin())
    filtered_df = df
    filtered_df = filtered_df[filtered_df[col] < val[0]]
    print(filtered_df.index[0])
    print(df.index[0])
    # print(df[col].head(10))
    # print(df[col].tail(10))
    # print(df.tail(10))
    # print(filtered_df)
    # print(df[df[col[0]]<val[0]]])
