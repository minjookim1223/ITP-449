# ITP 449 HW 1
# Minjoo Kim

# Q6. Write a program to compute and print all possible combinations of any value of money
# Denominations to be considered – quarter, dime, nickel, penny

try:
    money = float(input("Enter a dollar amount: "))

    print("Change for $" + str(money))
    for q in range(5):
        for d in range(11):
            for n in range(21):
                for p in range(101):
                    if 0.25 * q + .1 * d + .05 * n + 0.01 * p == money:
                        print(q, "quarters,", d, "dimes,", n, "nickels,", p, "pennies")

except ValueError:
    print("Please enter the a dollar amount.")