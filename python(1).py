list=[1,2,2,4,4,5,6,8,10,13,22,35,52,83]
new = []
new1 = []
for num in list:
    if num>=10:
        new.append(num)
print(new)
input=int(input("enter any given num : "))
for numb in list:
    if numb>input:
        new1.append(numb)
print(new1)
