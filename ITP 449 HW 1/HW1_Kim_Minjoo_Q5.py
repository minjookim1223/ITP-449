# ITP 449 HW 1
# Minjoo Kim

# Q5. Write a program to that prompts the user to enter a string.
# Then check whether or not the string is a palindrome.

string = input("Enter a string: ")
string = string.lower()

if string == string[::-1]:
    print(string + ", is a palindrome!")
else:
    print(string + ", is not a palindrome!")
