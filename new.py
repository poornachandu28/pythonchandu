employees=[{"name":"Tina",
          "birthday": "1990-03-10",
          'age': 30,
          "job": "Devops Engineer",
          "address": {"city":"new York","country":"USA"}
},
{ "name":"Tim",
  "birthday": "1985-02-21",
  'age': 35,
  "job": "Developer",
  "address": {"city":"Sydney","country":"Australia"}


}]

n=len(employees)
for i in range(n):
    print(employees[i]['name'],employees[i]['job'],employees[i]['address']['city'])

x=employees[1]['address']['country']
print("The second employees country is ",x)