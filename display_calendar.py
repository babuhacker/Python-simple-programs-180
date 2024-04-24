# program to Display Calendar

import calendar

year = int(input("enter year: "))
month = int(input("enter month: "))

calendar = calendar.month(year, month)
print(calendar)
