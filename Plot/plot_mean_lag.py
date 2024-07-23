import load_files as lf
from merge_open import merge_open
df = merge_open(lf.df_grouped)
import matplotlib.pyplot as plt
from val_list2index_list import  val_list2index_list

df.plot(x=0,y=1,kind="scatter")
# plt.show()
df.info()

df["y"] = df.iloc[:, 0].shift(-1)
df= df[-50:]
val_list2index_list(df,0,85,86)
df.plot(x=0,y="y", kind="scatter")
plt.show()