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