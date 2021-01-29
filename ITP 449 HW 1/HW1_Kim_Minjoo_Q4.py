# ITP 449 HW 1
# Minjoo Kim

# Q4. Write a program that prompts the user to enter a loan amount, annual interest rate,
# and number of years for a car loan. Then calculate and print the monthly payment amount.

try:
    PV = float(input("Loan Amount: "))
    i = float(input("Annual Interest Rate: ")) * 0.01 / 12
    years = int(input("Years: "))
    n = years * 12

    PMT = round((PV * i * (1 + i) ** n) / ((1 + i) ** n - 1), 2)

    print("Your monthly payment is: $" + "{:.2f}".format(PMT))

except ValueError:
    print("Try Again")
