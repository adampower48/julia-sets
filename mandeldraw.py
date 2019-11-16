import pandas as pd
import sys
import matplotlib.pyplot as plt

df = pd.read_csv(sys.stdin, na_values=-1, header=None)

plt.imshow(df)
plt.show()