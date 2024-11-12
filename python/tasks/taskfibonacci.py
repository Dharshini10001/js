# n1=0
# n2=1
# count=0
# while num>count:
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth
#     count+=1    

num=int(input("How many fibonacci number do you want?"))
def fibonacci(n1,n2):
    count=0
    while num > count:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+1
fibonacci(0,1)    