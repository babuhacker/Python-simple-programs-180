# program to Find the Sum of Natural Numbers

num = int(input("enter a limit: "))

if num < 0:
    print("please enter positive number")
else:
    sum = 0
    while num>0:
        sum += num
        num -= 1

    print(sum)

