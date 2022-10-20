class Student:
    def __init__(self, firstname, lastname, age, lectures):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.lectures = lectures

    def fullname(self, firstname, lastname):
        print("Full name:", self.firstname, self.lastname)
        print("age:",self.age)

    def List_lectures(self, lectures):
        print("List of lectures student attend:", self.lectures)

    def add_lectures(self, lectures):
        new_lec = input(" Add new list of lectures student attend :  ")
        new_lec1 = new_lec.split(" ")
        for i in new_lec1:
            self.lectures.append(i)
        print("New lectures list is:", self.lectures)

    def remove_lectures(self, lectures):
        remove_lec = input("Enter lectures u want to remove :    ")
        self.lectures.remove(remove_lec)
        print("Subjects list after removal is:", self.lectures)


first_name = input("Enter first name :   ")
last_name = input("Enter last name  : ")
age = input("Enter age :  ")
lectures = list(input('Enter lectures list he/she teaches :   ').split(" "))
s = Student(first_name, last_name, age, lectures)
s.fullname(first_name, last_name)
s.List_lectures(lectures)
s.add_lectures(lectures)
s.remove_lectures(lectures)




class Professor:
    def __init__(self, firstname, lastname, age, subjects):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.subjects = subjects

    def fullname(self, firstname, lastname):
        print("Full name:", self.firstname, self.lastname)

    def subjects_he_teaches(self, subjects):
        print("List of subjects he teach:", self.subjects)

    def add_subjects(self, subjects):
        new_sub = input("Enter new list of subjects to teach   ")
        new_sub1 = new_sub.split(" ")
        for i in new_sub1:
            self.subjects.append(i)
        print("New subjects list is:", self.subjects)

    def remove_subjects(self, subjects):
        remove_sub = input("Enter list of subjects to remove    ")
        self.subjects.remove(remove_sub)
        print("Subjects list after removal is:", self.subjects)

first_name = input("Enter first name    ")
last_name = input("Enter last name   ")
age = input("Enter age   ")
subjects = list(input('Enter subject list he teaches    ').split(" "))
print(subjects)
s = Professor(first_name, last_name, age, subjects)
s.fullname(first_name, last_name)
s.subjects_he_teaches(subjects)
s.add_subjects(subjects)
s.remove_subjects(subjects)


class Lecture:
    def __init__(self, name, max_no_of_students, duration, professor_list):
        self.name = name
        self.max_no_of_students = max_no_of_students
        self.duration = duration
        self.professor_list = professor_list

    def name_duration(self, name, duration):
        print("Name of the lecture is:", self.name, '\n', "Duration of the lecture in minutes is", self.duration)

    def new_professor_add(self, professor_list):
        new_prof = input("Enter new list of professors to teach   ")
        new_prof1 = new_prof.split(" ")
        for i in new_prof1:
            self.professor_list.append(i)
        print("Old and New professor list is:", self.professor_list)


name = input("Enter lecture name   ")
max_students = input(" Enter max no of students    ")
duration = input("Enter duration  in minutes   ")
professor_list = list(input('Enter  list of profs teach the subject   ').split(" "))
s = Lecture(name, max_students, duration, professor_list)
s.name_duration(name, duration)
s.new_professor_add(professor_list)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self, first_name, last_name):
        print("Person name is:", self.first_name, self.last_name)

class Student(Person):
    pass


class Professor(Person):
    pass

f_name = input("Enter student first name   ")
l_name = input("Enter student last  name   ")
age = input("Enter student age   ")
stu_obj = Student(f_name, l_name, age)
stu_obj.print_name(f_name, l_name)
f_name = input("Enter professor first name   ")
l_name = input("Enter professor last  name   ")
age = input("Enter professor age   ")
prof_obj = Professor(f_name, l_name, age)
prof_obj.print_name(f_name, l_name)