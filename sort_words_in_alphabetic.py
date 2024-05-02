# Program to Sort Words in Alphabetic Order

# a = "Harry potter and the Goblet of Fire"
a = input("enter something here: ")

w = a.split()
# print(w)
for i in range(len(w)):
    w[i] = w[i].lower()

# print(w)
    w.sort()
# print(w)
    for i in w:
        print(i)

