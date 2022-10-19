# import requests
# username = input("Enter the github username:")
# request = requests.get('https://github.com/poornachandu28/pythonchandu'+username+'/repos')
# json = request.json()
# for i in range(0,len(json)):
#   print("Project Number:",i+1)
#   print("Project Name:",json[i]['name'])
#   print("Project URL:",json[i]['svn_url'],"\n")
#
# import base64
# from github import Github
# from pprint import pprint
#
# g = Github
# user=g.ger_user(username)
# for repo in user.get_repos():
#     print(repo)
# class Student:
#     def __init__(self, firstname,lastname, age, lectures):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.lectures = lectures
#     def name(self,firstname,lastname):
#         print("Fullname :",self.firstname,self.lastname)
#         print("Age :",self.age)
#
#     def List_lectures(self,lectures):
#         print("List of lectures that he/she teaches :",self.lectures)
#
#     def add_lectures(self,lectures):
#         new_lec = input("if u want to add lecture add here : ")
#         new_lec1 = new_lec.split(" ")
#         for i in new_lec1:
#             self.lectures.append(i)
#         print("added list :",self.lectures)
#     def remove_lectures(self,lectures):
#         remove_lec = input("Enter the  lectures to remove    ")
#         self.lectures.remove(remove_lec)
#         print("lectures after removal ",self.lectures)
# first_name = input("Enter first name    ")
# last_name = input("Enter last name   ")
# age = input("Enter age   ")
# lectures = list(input('Enter the lectures list he/she teaches    ').split(" "))
# s = Student(first_name,last_name,age,lectures)
# s.name(first_name,last_name)
# s.List_lectures(lectures)
# s.add_lectures(lectures)
# s.remove_lectures(lectures)
from datetime import datetime
from datetime import date
import time

today = date.today()

def user_bday():
    year = int(input("Enter your year of birth[YY]"))
    month = int(input("Enter your birth month[MM]"))
    day = int(input("Enter your birth date[DD]"))
    print(f"Your date of birth is {day}-{month}-{year}")
    birthday = datetime(year, month, day)
    return birthday

def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        print("Your birthday comes next year again")
        return birthday
    else:
        return birthday

while True:
    try:
        Bdy = user_bday()
        t = calculate_dates(Bdy)
        time_to_birthday = abs(t - today)
        days = time_to_birthday.days
        current_time = datetime.now()
        h = current_time.hour
        m = current_time.minute
        s = current_time.second
        hours = (24-h)
        mins = (hours*60)
        secs = (mins*60)
        print(f'Time to your Birthday is {days} days / {hours} hours / {mins} minutes / {secs} seconds!!!')
    except:
        print("invalid input, Enter only numbers")
    user_input = input("do you want to continue Y/exit")
    if(user_input) == 'exit':
        break