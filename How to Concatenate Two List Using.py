# Program How to Concatenate Two List Using

# method 1 using + operator

l1 = [3, 6, 8, 2, "a", "j"]
l2 = [3, 6, "k", "f", "j"]

l12 = l1 + l2
print(l12)

# method 2 with unique values

l1 = [3, 6, 8, 2, "a", "j"]
l2 = [3, 6, "k", "f", "j"]

l12 = list(set(l1+l2))
print(l12)

# solution 3 using extend() function

l1 = [3, 6, 8, 2, "a", "j"]
l2 = [3, 6, "k", "f", "j"]

l1.extend(l2)
print(l1)
