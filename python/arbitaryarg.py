#arguments - when we don't know how many args will pass to function
# arbitary * argumants / functions - *args
def add(*args):
    print(args)
    result=sum(args)
    return result
myvar=add(1,2,3,4,5,5,6,7,7,8)
print(myvar)
# def fun(x,y):
#     print(x+y)
# myvar=fun(x=3,y=5)
# print(myvar)
# keyword word argument = when we don't know how many args will pass to function
# **
def function_name1(**args):
    print(args)
myvar=function_name1(fname="aaa",middlename="bbb",lastname="ccc")
print(myvar)

# default parameter - user over ride - default - pass accept
def add(a=7,b=6):
    # a=int(input("enter the value"))
    # b=int(input("enter the value2"))
    return a+b
myvar=add(4,3)
print(myvar)


def user(username="python"):
    print(username)
user("java")
user()
    # passing list in function
list1=[1,2,3,4,5]
def myfun(a,b,c,d,e):
    result=a+b+c+d+e
    return result
mylist=myfun(*list1)
print(mylist)

def listfun(numbers):
    result=sum(numbers)
    return result
myvar2=listfun([1,2,3,4,5,6])
print(myvar2)