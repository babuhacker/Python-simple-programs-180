# Python Program to Find Numbers Divisible by Another Number

# solution 1 using for loop
'''
n = int(input("enter number to divide"))
print("the numbers divisible by 13 are:")
for i in range(1, 100):
    if i % n == 0:
        print(i)
'''
# solution 2 using lambda function an

l = [39, 48, 26, 98, 33, 67, 87]
n = int(input("enter number to divide"))
result = list(filter(lambda x : x % n == 0, l))

print("the numbers divisible by 13 are", result)

