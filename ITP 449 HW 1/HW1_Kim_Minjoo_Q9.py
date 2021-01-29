# ITP 449 HW 1
# Minjoo Kim

# Q9. Given the score sheet of participants in a competition, you are required to find the runner-up score.
# You are given scores in a list. Find the score of the runner-up.

# Ex 1)
# list1 - [2, 3, 6, 6, 5]
# runner_up: 5

# Ex 2)
# list2 - [1, 7, 5, 3, 10, 4, 5, 5, 6, 11]
# runner_up: 10

list1 = [2, 3, 6, 6, 5]
list2 = [1, 7, 5, 3, 10, 4, 5, 5, 6, 11]

if len(set(list1)) > 1:
    print(sorted(set(list1))[-2])
else:
    print(list1[0])

if len(set(list2)) > 1:
    print(sorted(set(list2))[-2])
else:
    print(list2[0])