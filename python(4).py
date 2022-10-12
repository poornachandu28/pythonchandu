count=0
while True:
        b = int(input('first num: '))
        c = input('operator: ')
        d = int(input('second num: '))
        if c == '+':
            print(b,'+',d,'=',b+d)
            count+=1
        elif c == '-':
            print(b,'-',d,'=',b - d)
            count += 1
        elif c == '*':
            print(b,'*',d,'=',b * d)
            count += 1
        elif c == '/':
            print(b,'/',d,'=',b / d)
            count += 1
        q = input('do you want to continue?: ')
        if q == 'exit':
            # l.append([input(operator)])
            print(count)
            break
        else:
            continue
            
            
           
            
            ##########   output  #######
            
            
            
            
first num: 2
operator: +
second num: 2
2 + 2 = 4
do you want to continue?: n
first num: 5
operator: -
second num: 2
5 - 2 = 3
do you want to continue?: exit
2
        
            
            
