# Program to Return Multiple Values From a Function

# Solution 1 Using Tuples Unpacking

def friends():
    return "Joe", "Phoebe", "Monica"

print(friends())
n1, n2, n3 = friends()

print(n1, ",",  n1, "and", n3)


# Solution 2 Using a Dictionary

def friends():
    n1 = "Joe"
    n2 = "Phoebe"
    return {"a": n1, "b": n2}

names = friends()

print(names["a"], "and", names["b"])

