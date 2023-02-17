from datetime import datetime, date, timedelta

with open("today.txt", "r") as f:
    today_string = f.read().strip()
print(today_string)

today = datetime.strptime(today_string, "%H:%M %d.%m.%Y")
print(today)


birthday = date(2007, 6, 11)
print(birthday)
print(birthday.weekday())

tenk_days = timedelta(days=10000)
print(birthday + tenk_days)

