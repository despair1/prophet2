import load_files as lf
from merge_open import merge_open
from select_data import select_data
from select_data1 import select_data1

df = merge_open(lf.df_grouped)
# select_data(df,0)
select_data1(df,10,0)