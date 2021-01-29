# ITP 449 HW 1
# Minjoo Kim

# Q3. Write a program that prompts the user to enter a month (as a number),
# then prints the name of the month and the number of days in that month.
# Ensure that the user inputs a valid month and handle any error cases

long = {1: "January", 3: "March", 5: "May", 7: "July", 8: "August", 10: "October", 12: "December"}
short = {4: "April", 6: "June", 9: "September", 11: "October"}

month = input("Enter the month number: ")
if month[0] == "-":
    print("Enter a number between 1-12.")

elif month.isdigit():
    month = int(month)

    if month > 12 or month < 1:
        print("Enter any number between 1-12.")

    else:
        if month in long:
            print(long[month], "has 31 days.")
        elif month in short:
            print(short[month], "has 30 days.")
        else:
            print("February has 28 days or 29 days every four years.")

else:
    print("Your input is not a number.")
