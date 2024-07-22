import load_files as lf
from merge_open import merge_open
df = merge_open(lf.df_grouped)
import matplotlib.pyplot as plt
import pandas as pd

df.index = pd.to_datetime(df.index, format='%Y%m%d')
# df.iloc[:,0].plot()
df.plot()
df.info()
plt.show()