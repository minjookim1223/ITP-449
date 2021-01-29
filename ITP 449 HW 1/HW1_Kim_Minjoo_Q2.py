# ITP 449 HW 1
# Minjoo Kim

# Q2. Write a program that prompts the user to enter their full name
# then prints the number of characters in their name (do not count spaces)

name = input("What is your name? ")
count = 0

for char in name:
    if char != " ":
        count += 1

print(name, "your name has", count, "characters.")