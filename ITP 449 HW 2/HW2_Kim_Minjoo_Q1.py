# ITP 449 HW 2
# Minjoo Kim

import pandas as pd

data = {"name": ["Joseph", "Jacob", "Sam", "Jesee", "Ryan", "Lisa", "Lee"],
        "job": ["teacher", "psychologist", "data scientist", "software developer", "psychologist",
                "psychologist", "teacher"],
        "family_size": [3, 2, 1, 4, 2, 3, 2],
        "num_cars": [3, 1, 1, 2, 2, 4, 1]}

# Q1-1: Write a program that create a dataframe from the data.
names = pd.DataFrame(data)
print(names, "\n\n")


# Q1-2: Select people that are psychologist or teacher and their number of cars is greater than their family size.
cond_psych = names["job"] == "psychologist"
cond_teach = names["job"] == "teacher"
cond_cars = names["num_cars"] > names["family_size"]

q2 = names.loc[(cond_psych | cond_teach) & cond_cars]
# q2 = names[(cond_psych | cond_teach) & cond_cars]
print(q2, "\n\n")


# Q1-3: Select people who have at most 2 family members and at least 1 car.
fam_size = names["family_size"] <= 2
num_cars = names["num_cars"] >= 1

# q3 = names[fam_size & num_cars]
q3 = names.loc[fam_size & num_cars]
print(q3, "\n\n")


# Q1-4: Write a code that get number of unique jobs in this dataset.
# no_dupe = names["job"].drop_duplicates()
no_dupe = names.loc[:, "job"].drop_duplicates()
print(no_dupe, "\n\n")