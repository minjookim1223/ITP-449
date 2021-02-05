# ITP 449 HW 2
# Minjoo Kim

import numpy as np

# Q5: Write a numpy program to print sum of all the multiples of 3 or 5 below 100
spectrum = np.arange(1, 100)
print(spectrum[(spectrum % 3 == 0) | (spectrum % 5 == 0)])
