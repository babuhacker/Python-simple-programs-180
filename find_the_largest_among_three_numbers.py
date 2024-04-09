# Program to Find the Largest Among Three Numbers

num1 = int(input("enter 1st number here: "))
num2 = int(input("enter 2nd number here: "))
num3 = int(input("enter 3rd number here: "))

if (num1 > num2) and (num1 > num3):
    print(num1, "is the largest")

elif (num2 > num1) and (num2 > num3):
    print(num2, "is the largest")

else:
    print(num3, "is the largest")


