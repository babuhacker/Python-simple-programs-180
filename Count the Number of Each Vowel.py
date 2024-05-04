# Program to Count the Number of Each Vowel
# Solution 1 using Dictionary

'''

a = "Harry Potter and the Prisoner of Azkaban"

vowels = "aeiou"

a = a.casefold()
print(a)
count = {}.fromkeys(vowels, 0)

for char in a:
    if char in count:
        count[char] += 1
print(count)

'''

# Solution 1 using

string = input("Enter sentence here: ")

# string = "Harry Potter and the Prisoner of Azkaban"
vowels = "aeiou"
string = string.casefold()

count = {key: sum([1 for char in string if char == key]) for key in vowels}

print(count)

