employee={"name":"tim",
          "birthday": "1990-03-10",
          'age': 30,
          "job": "DevOps Engineer"
}
employee.pop('age')
employee['job'] = 'Software Engineer'
for key, value in employee.items():
    print(key,':',value)
