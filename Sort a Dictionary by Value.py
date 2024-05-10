# Program to Sort a Dictionary by Value

# Solution 1 Dictionary by value

marks = {"john": 23, "Lisa": 56, "Sid": 48}
print(marks)

sv = sorted(marks.items(), key=lambda x: x[1])
print(sv)

# Solution 2 short only the values

v = sorted(marks.values())
print(v)
