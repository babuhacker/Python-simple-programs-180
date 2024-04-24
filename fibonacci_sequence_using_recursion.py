# program to Display Fibonacci Sequence Using Recursion

n = int(input("enter a number here: "))


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

if n <= 0:
    print("enter a positive number: ")
else:
    print("Fibonacci Sequence")
    for i in range(n):
        print(fibo(i))
