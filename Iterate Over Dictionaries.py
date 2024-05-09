# Program to Iterate Over Dictionaries Using For Loop

friends = {"Rachel":"Ross", "Monica":"Chandler","Phoebe":"Joe"}
print(friends)

# Solution 1 with .items

for key,value in friends.items():
    print(key, "-", value)


# Solution 2 with keys

for key in friends:
    print(key,"-",friends[key])

# Solution 3 with keys and values

for key in friends.key():
    print(key)

for i in friends.values():
    print(i)
