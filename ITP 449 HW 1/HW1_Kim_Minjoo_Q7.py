# ITP 449 HW 1
# Minjoo Kim

# Q7. Ask the user to enter two positive integers between 1 and 100. Read those integers.
# Then output a multiplication table of the first number times the second number.
# Note: You have to ensure the entered numbers are between 1 and 100 only.

num = ""
number = ""

while not num.isdigit() or not number.isdigit():
    num = input("Please enter an integer: ")
    number = input("Please enter another integer: ")

    if num.isdigit() and number.isdigit():
        num = int(num)
        number = int(number)
        if 0 <= num <= 100:
            if 0 <= number <= 100:
                break
    else:
        print("Enter two integers from 1-100")

for i in range(1, number + 1):
    print(num, "x", i, "=", num * i)
