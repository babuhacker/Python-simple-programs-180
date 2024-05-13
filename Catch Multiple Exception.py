# Program to Catch Multiple Exception
# Solution  (handling multiple exceptions)

string = input("enter a number here: ")

try:
    num = int(input("enter a number here: "))
    print(string + num)
except(ValueError, TypeError) as a:
    print(a)
