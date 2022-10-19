from datetime import datetime
from datetime import date
import time

today = date.today()

def user_birthday():
    year = int(input('When is your birthday? [Year] : '))
    month = int(input('When is your birthday? [Month] : '))
    day = int(input('When is your birthday? [Day] : '))
    birthday = datetime(year, month, day)

    return birthday

def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday

    elif birthday > today:
        birthday = birthday.replace(year=today.year,day=birthday.day-1)
        return birthday
    elif birthday==today:
        print("Happy Birthday "
              "tody is your birthday  ")
        birthday = birthday.replace(year=today.year)
        return birthday

bday = user_birthday()
t = calculate_dates(bday)
time_to_birthday = abs(t - today)
days = str(time_to_birthday.days)
current_time = datetime.now()
h = current_time.hour
m = current_time.minute
s = current_time.second
n=(24-h)
x=(60-m)
m=(60-s)

print(f"Time to Birthday is  {days} days,")
print(f"{n}  hours left and")
print(f"{x}  minutes left and,")
print(f"{m} seconds")