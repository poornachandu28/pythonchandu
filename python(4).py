loop = 0
loop = 1
count = 0
choice = 0
while loop == 1:
    print(" Hey user your options are Here, please choose anyone:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("choose your option(1,2,3,4): ")
    try:
        if choice == '1':
             n1 = int(input("Enter the First Number: "))
             n2 = int(input("Enter the Second Number: "))
             print(n1, "+", n2, "=", n1 + n2)
             count += 1
        elif choice == '2':
             n1 = int(input("Enter the First Number: "))
             n2 = int(input("Enter the Second Number:"))
             print(n1, "-", n2, "=", n1 - n2)
             count += 1
        elif choice == '3':
             n1 = int(input("Enter the First Number: "))
             n2 = int(input("Enter the Second Number: "))
             print(n1, "*", n2, "=", n1 * n2)
             count += 1
        elif choice == '4':
            n1 = int(input("Enter the First Number: "))
            n2 = int(input("Enter the Second Number: "))
            print(n1, "/", n2, "=", n1 / n2)
            count += 1
        elif choice == 'exit':
            loop = 0
            print("The number of calculations user did:", count)
        else:
            print("%d is not valid input. Please enter the correct option." % choice)
    except Exception:
        print(" your output is undefine ")
    except ValueError and TypeError:
        print("%r is not valid input.  Please enter 1, 2, 3, 4." % choice)
        
        
        
        
        
        
        
        #######  output  #####
        
        
       
    
 Hey user your options are Here, please choose anyone:
1. Addition
2. Subtraction
3. Multiplication
4. Division
choose your option(1,2,3,4): 1
Enter the First Number: 2
Enter the Second Number: 4
2 + 4 = 6
 Hey user your options are Here, please choose anyone:
1. Addition
2. Subtraction
3. Multiplication
4. Division
choose your option(1,2,3,4): 2
Enter the First Number: 5
Enter the Second Number:3
5 - 3 = 2
 Hey user your options are Here, please choose anyone:
1. Addition
2. Subtraction
3. Multiplication
4. Division
choose your option(1,2,3,4): exit
The number of calculations user did: 2
continue (yes/no): no
