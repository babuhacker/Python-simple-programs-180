# Program to Check Whether a String is Palindrome or Not

a = input("Enter a word here: ")

rev =  a[::-1]

if a == rev:
    print("It is a palindrome number")
else:
    print("It is not palindrome")
