# ITP 449 HW 1
# Minjoo Kim

# Q8. Write a program to ask the user to enter a password.
# Then check to see if it is a valid password based on these requirements -
#
# 1) Must be at least 8 characters long
# 2) Must contain both uppercase and lowercase letters
# 3) Must contain at least one number between 0-9
# 4) Must contain a special character -!,@,#,$
#
# If the password is not valid, ask the user to re-enter.
# This should continue until the user enters a valid password.
# After a valid password is entered, print Access Granted!

print("Please enter a password. Follow these requirements - ")
print("a. Must be at least 8 characters long")
print("b. Must contain both uppercase and lowercase letters")
print("c. Must contain at least one number between 0-9")
print("d. Must contain a special character -!,@,#,$")

granted = False

while not granted:
    password = input("Password: ")

    length = len(password) >= 8
    num, special, upper, lower = False, False, False, False

    for i in password:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            num = True
        if i in ["!", "@", "#", "$"]:
            special = True

    # if not length:
    #   print("Your password is less than 8 characters.")
    # if not upper:
    #   print("Your password does not have an upper case")
    # if not lower:
    #   print("Your password does not have a lower case")
    # if not num:
    #   print("Your password does not have a number")
    # if not special:
    #   print("Your character does not have a special character.")

    if num and special and length and upper and lower:
        break
    else:
        print("Invalid Password. Try again!")

print("Access Granted!")
