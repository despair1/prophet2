import load_files as lf
from merge_open import merge_open
df = merge_open(lf.df_grouped)
import matplotlib.pyplot as plt
import pandas as pd

df.info()

print(df.mean())
print(df.var())