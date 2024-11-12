'''
1.addition
2.subtract
3.multiple
4.division
5.modulus
6. floor
7. exponatial
8.campare
9. bitwise AND
10.bitwise OR
11.Bitwise Xor
12.bitwise Not
13.exit
'''

while True:
    option = int(input("Enter the operation you want or click 100:"))
    if option ==1:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:")) 
        def add():
            print(item1+item2)
        add()   
    elif option == 2:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def sub():
            print(item1-item2)
        sub() 
    elif option == 3:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def mul():
            print(item1*item2)
        mul()
    elif option ==4:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def div():
            print(item1/item2)
        div()
    elif option == 5:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def modulus():
            print(item1%item2)
        modulus()
    elif option == 7:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def expontial():
             print(item1**item2)
        expontial()
    elif option == 6:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def floor():
            print(item1//item2)
        floor()
    elif option == 8:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def compare():
            if item1 >item2:
                print(f"{item1} is greater than {item2}")
            else:
                print("")
            compare()
    elif option == 9:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def And():
            print(item1 & item2)
        And()
    elif option == 10:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def Or():
            print(item1|item2)
        Or()
    elif option == 11:
        item1=int(input("Enter the first number:"))    
        item2=int(input("Enter the second number:"))
        def Xor():
            print(item1*item2)
        Xor()
    elif option == 12:
        item1=int(input("Enter the first number:"))  
        item2=int(input("Enter the second number:"))
        def Not():
            print(~item1)
            print(~item2)
        Not()
    else:
        print("Invalid input!")
        break
    
