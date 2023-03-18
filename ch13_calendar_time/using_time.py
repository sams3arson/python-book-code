import time

# time.time() = unix time
now = time.time()
print(now, type(now))

# time.ctime = unix time to string
print(time.ctime(now), type(time.ctime(now)))

# time.localtime = current time в объект struct_time, с которым удобно работать (локальное время)
# можно передать значение в формате unix time
print(time.localtime(now))

# time.gmtime = тоже самое, но по utc
# можно передать значение в формате unix time
print(time.gmtime(now))

# tm_isdst - летнее время [0 или 1; -1 = неизвестно]
# к атрибутам объекта struct_time можно обращаться по именам (like named tuple)

# time.mktime - из объекта struct_time в unix_time
tm = time.localtime()
print(time.mktime(tm))

# using strftime: see strftime.png for more details or just google it
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t)) # 1 = строка форматирования, 2 = объект struct_time

from datetime import date as dt_date
some_day = dt_date(2019, 7, 4)
print(some_day.strftime(fmt)) # time is being set to 12am of only date is provided

from datetime import time as dt_time
some_time = dt_time(10, 35)
print(some_time.strftime(fmt)) # date is being set to 01-01-1900 of only time is provided

# strptime = from string to date/time/struct_time object
fmt = "%Y-%m-%d"
try:
    print(time.strptime("2019 01 29", fmt)) # string must exactly match the format
except ValueError as e:
    print(e)
print(time.strptime("2019-01-29", fmt))

