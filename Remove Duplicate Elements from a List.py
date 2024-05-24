# Program to Remove Duplicate Elements from a List

n = int(input("enter the total no of elements you want inside your list: "))
l = []
for i in range(n):
    ele = input("Enter the element")
    l.append(ele)

print("My list ", l)
non_duplicate_values = set(l)
print(non_duplicate_values)
