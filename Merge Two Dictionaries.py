# Merge Two Dictionaries
# Solution 1 using | Operator

# dict1 = {"John": 89, "Lisa": 99}
# dict2 = {"Lisa": 94, "Peter": 78}

# print(dict1 | dict2)

# solution 2 using ** Operator

# dict1 = {"John": 89, "Lisa": 99}
# dict2 = {"Lisa": 94, "Peter": 78}

# print({**dict1, **dict2})


# Solution 3 using Copy() and Update() methods

dict1 = {"John": 89, "Lisa": 99}
dict2 = {"Lisa": 94, "Peter": 78}
dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)
