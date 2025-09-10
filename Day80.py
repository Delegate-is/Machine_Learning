# Python Date Object
# Time module is used to work with time-related tasks.
import time
# Datetime module is used to work with date and time in more flexible way.
# Classes like date, time, datetime, timedelta, timezone are defined in this module.
# time() function of time module returns the current time in seconds since epoch.
print("Time in seconds since epoch:", time.time())
# localtime() function of time module returns the current local time.
print("Local time:", time.localtime())
# asctime() function of time module converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string of the following form: 'Sun Jun 20 23:21:05 1993'.
print("Current time:", time.asctime())
# sleep() function of time module suspends (delays) execution of the current thread for the given number of seconds.
print("Sleeping for 5 seconds...")
time.sleep(5)
print("Awake now!")
# ctime() function of time module converts a time expressed in seconds since epoch to a string representing local time.
print("Current time using ctime():", time.ctime())



from time import time, ctime, sleep, localtime, asctime
print("Time in seconds since epoch:", time())
print("current time:", ctime())
obj = localtime()
print("Local time:", obj.tm_year)
print("Local time:", obj.tm_mon)
print("Local time:", obj.tm_mday)
print("Local time:", obj.tm_hour)


# datetime module used to work with date and time in more flexible way.
# Classes like date, time, datetime, timedelta, timezone are defined in this module.
# date class is used to manipulate the date.
# today() function of date class returns the current local date.
# time class is used to manipulate the time.
# datetime class is used to manipulate both date and time.

import datetime
x = datetime.datetime.now()
print(x)

from datetime import date, time, datetime, timedelta
dt = date.today()
print(dt.month)
print(date(2023, 6, 20))
tm = time(12, 30, 45, 325)
print(tm.hour)
c_dt = datetime.now()
print(c_dt)
print("After manipulation:", c_dt + timedelta(days=5, hours=3, minutes=20))

print(timedelta(days=5, weeks=1, hours=3, minutes=20))

# program to display different Date Time formats
from datetime import datetime
now = datetime.now()
print("Current date and time:", now)

# Program to get two dates and find the difference between them
from datetime import date
f_date = date(2023, 6, 20)  # first date
l_date = date(2024, 6, 20)  # later date
delta = l_date - f_date
print("Difference between two dates:", delta.days)

y1 = int(input("Enter first year: "))
y2 = int(input("Enter second year: "))
m1 = int(input("Enter first month: "))
m2 = int(input("Enter second month: "))
d1 = int(input("Enter first day: "))
d2 = int(input("Enter second day: "))
date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)
delta = date2 - date1
print("Difference between two dates:", delta.days)
dt1 = date(2023, 6, 20)
dt2 = date(2024, 6, 20)
dt = dt2 - dt1
print("Difference between two dates:", str(dt.days))

# Program to get age in years and convert it to seconds
from datetime import date
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
birth_date = date(2000, 6, 20)
age = calculate_age(birth_date) # age in years
print("Age in years:", age)

age1 = float(input("Enter your age in years: "))
age_in_seconds = age1 * 365 * 24 * 60 * 60
print("Your age in seconds is:", age_in_seconds)

def days_until_birthday(birthday):
    today = date.today()
    next_birthday = date(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birthday.month, birthday.day)
    delta = next_birthday - today
    return delta.days
birthday = date(2000, 6, 20)
days_left = days_until_birthday(birthday) # days until next birthday
print("Days until next birthday:", days_left)
