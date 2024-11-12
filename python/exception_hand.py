#exception handling
# some error occurs - handle -
# 3 types 
# complile time error
# logical error
# runtime error
# compile time error - syntax
# print("python")
# # printt("hello")
# # logical error
# a=4
# b=5
# print(a+a) #logical mistake
# runtime error
# try:
#     a=int(input("enter the number1"))
#     b=int(input("enter the number2"))
#     print(a,b)
# except:
#     print("something wrong")
try:
    a=int(input("enter the values:"))   
    b='5'
    print(b/a)
except ValueError as e:
    print("value error",e) 
except NameError as e:
    print("Name error",e)
except Exception as e:
    print(e)
else:
    print("sucessfully")
finally:
    print("done")