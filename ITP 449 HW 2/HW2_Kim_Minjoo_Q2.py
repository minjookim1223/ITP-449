# ITP 449 HW 2
# Minjoo Kim

import pandas as pd
import numpy as np

# Q2. Lets consider you have two series like below. Compute the mean of weights of each fruit.
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

df = pd.DataFrame({"fruits": fruit, "weights": weights})
df_mean = df.groupby("fruits").mean()
print(df_mean)