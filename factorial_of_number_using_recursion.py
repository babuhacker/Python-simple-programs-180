# Program to Find Factorial of Number Using Recursion

def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

n = int(input("enter a number here: "))

if n <= 0:
    print("factroial of number less than 1 does not exists")
else:
    print("factorial if given number is", fact(n))
