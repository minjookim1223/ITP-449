# ITP 449 HW 2
# Minjoo Kim

import numpy as np

# Q6. Consider the below array.
arr = np.arange(12).reshape(3,4)
print(arr, "\n")

# Q6.1. Write a code to swap column 1 with column 2.
column = arr[:, [1]]
arr[:, [1]] = arr[:, [2]]
arr[:, [2]] = column
print(arr, "\n")

# Q6.2. Write a code to swap row 0 with row 1.
row = arr[[0], :]
arr[[0], :] = arr[[1], :]
arr[[1], :] = row
print(arr)