#Python has a module named datetime to work with dates and times.
import datetime

#Get Current Date and Time
datetime_object = datetime.datetime.now()
print("Current Date and Time",datetime_object)

#Get current date
date_object = datetime.date.today()
print("current date:",date_object)

#List all modules of module
print(dir(datetime))

#Date object to represent a date
d = datetime.date(2019, 4, 13)
print("Type of d:",type(d),", Date Object Value:",d)

from datetime import date

#Creating the date object from current date
today = date.today()
print("Type of today:",type(today),"Current date =", today)

#Print today's year, month and day
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

print("----------------Time------------------")
#Time object to represent time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("Time1 =", a)
# time(hour, minute and second)
b = time(11, 34, 56)
print("Time2 =", b)
# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("Time3 =", c)
# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("Time4 =", d)
#Print hour, minute, second and microsecond
print("hour =", d.hour)
print("minute =", d.minute)
print("second =", d.second)
print("microsecond =", d.microsecond)

print("----------------Time Delta------------------")
#timedelta:A timedelta object represents the difference between two dates or times.
from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

#Difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)
print("type of t3 =", type(t3))
print("type of t6 =", type(t6))

#negative timedelta object
t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))

print("----------------Date Format------------------")
#Python format datetime: Python has strftime() and strptime() methods
#strftime:creates a formatted string from a given date, datetime or time object.
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

#strptime() method creates a datetime object from a given string (representing date and time).
date_string = "21 June, 2019"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

#Handling Time Zone in Python
print("---------------Timezone in Python-----------------")
#Can be handled using a third-party module: pytZ module.
# Command Line: pip install pytz
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
