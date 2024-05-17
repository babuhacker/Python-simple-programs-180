# Program to Convert String to DateTime

# Solution 1 using datetime module

from datetime import datetime

date = "oct 14 1997 7:15AM"

date_time = datetime.strptime(date, "%b %d %Y %I :%M%p")
print(date_time)
print(type(date_time))

# Solution 2 using dateutil Module

from dateutil import parser

date_time = parser.parse("Oct 14 1997 7:15 AM")

print(date_time)
print(type(date_time))
