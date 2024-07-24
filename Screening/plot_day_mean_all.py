from  load_csv_walk import load_csv_walk
from group_by_day import group_by_day

dfs = load_csv_walk()

dfs = group_by_day(dfs)
print(dfs)
