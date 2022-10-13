#######   youngest employeee #########

def list(my_list):
    if my_list[0]['age'] < my_list[1]['age']:
        print("name of youngest employee:", my_list[0]['name'])
        print("age of youngest employee:", my_list[0]['age'])
    else:
        print("name of youngest employee:", my_list[1]['name'])
        print("age of youngest employee:", my_list[1]['age'])


list1 = [{"name": "Tina", "age": 30, "birthday": "1990-03-10", "job": "Devops Engineer",
         "address": {"city": "New York", "country": "USA"}},
         {"name": "chandu", "age": 23, "birthday": "2000-09-28", "job": " Associate Engineer",
         "address": {"city": "Hyderabad", "country": "India"}}]

list(list1)


########  even numbers from accept list   ########


def even_numbers():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list:
        if i%2 == 0:
            print(i)
even_numbers()


#######   checking upper and lower case letters ######


def letters(word):
    upper_letters=0
    lower_letters = 0
    for i in word:
        if(i.isupper()):
            upper_letters +=1
        elif(i.islower()):
            lower_letters +=1
    print("upper:", upper_letters)
    print("lower:", lower_letters)

word = input("Enter a string: ")
letters(word)
