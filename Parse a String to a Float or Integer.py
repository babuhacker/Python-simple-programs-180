# Program to Parse a String to a Float or Integer

# Solution 1 parse string into Integer

# string = "12345"
# print(type(string))
# int_str = int(string)
# print(type(int_str))

# Solution 2 parse string into float

# string = "123.45"
# print(type(string))
# print(string)
# float_string = float(string)
# print(type(string))
# print(float_string)

# Solution 3 parse string float numeral into Integer

string = "123.45"
print(type(string))
str_float_int = int(float(string))
print(type(str_float_int))
