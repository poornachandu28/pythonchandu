# count=0
# while True:
#         b = int(input('first num: '))
#         c = input('operator(+,-,*,/):  ')
#         d = int(input('second num: '))
#         if c == '+':
#             print(b,'+',d,'=',b+d)
#             count+=1
#         elif c == '-':
#             print(b,'-',d,'=',b - d)
#             count += 1
#         elif c == '*':
#             print(b,'*',d,'=',b * d)
#             count += 1
#         elif c == '/':
#             print(b,'/',d,'=',b / d)
#             count += 1
#         q = input('do you want to continue?: ')
#         if q == 'exit':
#             # l.append([input(operator)])
#             print(count)
#             break
#         else:
#             continue



# def get_youngest_employee(self, employees):
#     ages = {}
#     for idx,e in enumerate(employees):
#         ages[idx] = e['age']
#     return employees[min(ages, key=ages.get)]
#

def even_numbers():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list:
        if i%2 == 0:
            print(i)


