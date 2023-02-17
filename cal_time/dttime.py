from datetime import date

hween = date(2019, 10, 31) # order: y, m, d
print(hween.day, hween.month, hween.year)
print(hween.isoformat()) # iso 8601

today = date.today()
print(today)

# timedelta - используем для того, чтобы прибавить к объекту типа date
# некоторый временной интервал
from datetime import timedelta
one_day = timedelta(days=1)
print(one_day, type(one_day))
tomorrow = today + one_day
print(tomorrow)

print(today + 17 * one_day) # объекты timedelta можно прибавлять, вычитать, умножать (и даже делить)

yesterday = today - one_day
print(yesterday)

# границы:
print(date.min, date.max)


# time
from datetime import time
noon = time(12, 0, 0) # order: hour, minute, second, microsecond; all optional
print(noon)
print(noon.hour, noon.minute, noon.second, noon.microsecond)


# datetime: date and time in one object
from datetime import datetime
some_day = datetime(2019, 1, 2, 3, 4, 5, 6) # order: y, m, d, hr, min, sec, microsec
print(some_day)
print(some_day.isoformat())

now = datetime.now()
print(now)
print(now.day, now.month, now.year, now.hour, now.minute, now.second, now.microsecond)

# datetime.combine - объединяет объекты date и time в один объект datetime
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon) # 1 - date, 2 - time
print(noon_today)

# и обратно:
noon_date = noon_today.date()
noon_time = noon_today.time()
print("date:", noon_date, "time:", noon_time)

