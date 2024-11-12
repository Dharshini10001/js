# positional statements

# def function_name(n):
#     print(n)
# function_name(3)

# def function_name1(n):
#     print(n)
# function_name(n=3)
# / - *
# *- positional argument

# def function_name(*,n): #before
#     print(n)
# function_name(n=3)

# def function_name(n,/): #after
#     print(n)
# function_name(3)

# rescursive function - which function is called itselt 
# def myfunction():
#     myfunction()/ called itself
# myfunction
# example:
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

num=int(input("How many fibonacci number do you want?"))
def fibonacci(n1,n2):
    count=0
    if num<=0:
        print("You entered negative value")
    else:
        while num>count:
            nth = n1+n2
            n1=n2
            n2=nth
            count+=1
            print(n1)
fibonacci(0,1)
        
# nested function
# function - inside function
def funct_1(num):#outer function
    def funct_2(num1): #inner function
        print(num1)
    funct_2(num)#outer - call
print(funct_1(num=5))
# funct_2() - inside block
# funct_2() - undefined