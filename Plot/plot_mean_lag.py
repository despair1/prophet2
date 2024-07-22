import load_files as lf
from merge_open import merge_open
df = merge_open(lf.df_grouped)
import matplotlib.pyplot as plt

df.plot(x=0,y=1,kind="scatter")
plt.show()
df.info()

df["y"] = df.iloc[:, 0].shift(-1)
df= df[-50:]
df.plot(x=0,y="y", kind="scatter")
plt.show()