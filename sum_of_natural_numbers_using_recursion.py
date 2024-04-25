# Program to Find the Sum of Natural Numbers Using Recursion

# nns = natural number sum
def nns(n):
    if n <= 1:
        return n
    else:
        return(n) + nns(n-1)

n = int(input("enter a number here: "))

if n <= 0:
    print("enter a positive number: ")
else:
    print("the sum of natural number upto given number is: ", nns(n))
