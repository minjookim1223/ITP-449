# ITP 449 HW 2
# Minjoo Kim

import numpy as np

# Q4. Consider the below student_id array:
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])

# Q4-1: Reverse the student_id array. Print both original and reversed array.
print(student_id[::-1])

# Q4-2: Get the 3-largest values of student_id array.
sorted_students = np.sort(student_id)
print(sorted_students[-3:])