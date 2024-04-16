# program to print Fibonacci Sequence using for loop
num = int(input("enter a number to obtain Fibonacci Sequence: "))
a = 0
b = 1

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a+b
        a = b
        b = c
        print(c)

