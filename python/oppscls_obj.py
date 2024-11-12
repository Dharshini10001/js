#class and objects
# class it blueprint of object 
# object - real world - object - water bottle - labtop - human - place 
# class - object
# class myclass:
#     pass # empty class
# class mall:
#     def cinema(self):
#         print("welcome to my cinema")
#     def shooping(self):
#         print("hank you for shopping")
#     def game(self):
#         print("play station")
#     # 3 friend 
#     # anitha - games 
#     # akalya - shopping
#     # deepika - cinema
# anitha=mall()
# akalya=mall()
# deepika=mall()
# print(anitha.game())
# print(akalya.shooping())
# print("akalya cinema",deepika.cinema())
# print("after cinema akalya go to see anitha",deepika.game())
# class computer:
#     ram="0bg"
#     processor=0
#     price=0
#     def display(self):
#         print("displaying computers")
# hp=computer()
# hp.ram="5gb"
# hp.price=50000
# print(hp.ram)
# print(hp.price)
# print(hp.display())
# dell=computer()
# print(dell.price)
# class myclass:
#     def __init__(self): #initializer-class contructor - class - method - when i created object to my class - 
#         # that time contructor clss 
#         #call utomatiically
#         print("constructor class")
#     def display(self):
#         print("display method")
# obj=myclass()
# obj.display()

# task1

# class student:
#     name = "Dharshini"
#     age = 20
#     grade = "A"
#     def info(self):
#         print("your name: " ,name)
#         print("Age is: ",age)
#         def __init__(self): 
#            print("update your grade: ")
#     def shooping(self):
#         print("hank you for shopping")
#     def game(self):
#         print("play station")
    # 3 friend 
    # anitha - games 
    # akalya - shopping
    # deepika - cinem
# Dharshini=student()
# Akalya=student()
# abi=student( )
# print(Dharshini.info( ))
# print(Akalya.update())
# print("akalya cinema",abi.info())

# 

# class student_info:
#     def name(self):
#         print("welcome to my cinema")
#     def age(self):
#         print("Thank you for shopping")
#     def __init__(self): 
#            print("update your grade: ")
    # 3 friend 
    # anitha - games 
    # akalya - shopping
    # deepika - cinema
# anitha=student_info()
# akalya=student_info()
# deepika=student_info()
# print(anitha.name())
# print(akalya.age())



class student:
    name=""
    age=0
    grade="A"
    def info(self):
        print("student information")
abi=student()
abi.name="Dharshini"
abi.age=20
print(abi.info())
print("First student name: ",abi.name)
print("Student age: ",abi.age)
print("Student grade: ",abi.grade)
anitha=student()
print("Second student name: ",anitha.name)
print("SecondStudent age: ",anitha.age)
print("Second Student grade: ",anitha.grade)

