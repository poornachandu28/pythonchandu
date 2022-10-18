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
    else:
        return birthday


bday = user_birthday()
t = calculate_dates(bday)
time_to_birthday = abs(t - today)
days = str(time_to_birthday.days)
n=int(days)*24

print(f"Time to Birthday is  {days} days,")
print(f"{n}  hours and")
print(f"{n*60}  minutes,")
print(f"{n*60*60} seconds")



