# program to Convert Decimal to Binary Using Recursion

def convertbinary(n):
    if n > 1:
        convertbinary(n//2)
    print(n % 2, end="")


n = int(input("enter a number here: "))
print("the binary of the given number is: ")
convertbinary(n)

