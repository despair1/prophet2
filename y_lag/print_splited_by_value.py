import init
from day_mean_all_ofz import day_mean_all


df = day_mean_all()
indexes = {}
for key,val in init.split_by_decreasing_values.items():
    col = [col for col in df.columns if key  in col]
    if not col: continue
    if len(col) !=1: continue
    print(col, val[0])
    ind = []
    filtered_df = df
    col = col[0]
    ind.append(df.index[0])
    for i in val:
        filtered_df = df[df[col] < i]
        ind.append(filtered_df.index[0])
        print(i)
    ind.append(df.index[-1])
    print(ind)
    if len(ind) < 2: continue
    start_i = ind[0]
    idx = ind[1:]
    for i in idx:
        print(start_i,i)
        # print(df.loc[start_i:i])
        start_i=i
    indexes[key]=ind
print(indexes)



