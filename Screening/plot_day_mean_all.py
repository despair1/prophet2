import matplotlib.pyplot as plt
from day_mean_all_ofz import day_mean_all

df = day_mean_all()
df.plot()
# df[-50:].plot()
print(df)
plt.show()
