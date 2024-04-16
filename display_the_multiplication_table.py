# program to Display the Multiplication Table

# solution one using loop method
'''
num = int(input("enter a number here: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)
'''

# solution second using while loop method

num = int(input("enter a number here: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1
