# ITP 449 HW 2
# Minjoo Kim

import numpy as np

# Q3. Consider the below course_name array:
course_name = np.array(['Python', 'JS', 'examples', 'PHP', 'html'])

# Q3-1: Write a NumPy program to get the indices of the sorted elements of course_name array.
i = np.argsort(course_name)
print("Indices of the sorted elements of course_name array: ")
print(i, "\n")

# Q3-2: Write numpy code to check whether each element of course_name array starts with "P".
print(np.char.startswith(course_name, "P"))
