# Program to Accessing Index of List using for Loop
# Solution 1 using Enumerate method

# l = [34, 5, 61, 54, 89]

# for index, value in enumerate(l:
  #   print(index, "-",  value)

# Solution 2 using for loop

l = [34, 5, 61, 54, 89]

print(l[3])
for index in range(len(l)):
    value = l[index]
    print(index, "-", value)


