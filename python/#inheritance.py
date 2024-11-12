#inheritance- code reusablity 
#dad to son - two invidual - son - 
# base clss - new drive - inheritance
# child class is  derived from parents class
# dad- base class
# son - child /dirived class 
# 
# single in heritance 
# class dad():
#     def mobile(self):
#         print("mobile")
# class son(dad):
#     def labtop(self):
#         print("labtop")
# son1=son()
# son1.labtop()
# son1.mobile()

# # multiple inheritance
# class dad():
#     def mobile(self):
#         print("mobile")
# class mom():
#     def chocolates(self):
#         print("chocolate")
# class son(dad,mom): #multiple - one child class is derived from more than one parent class
#     def labtop(self):
#         print("labtop")
# son1=son()
# son1.labtop()
# son1.mobile()
# son1.chocolates()
# multi-level inheritance 
# granfather - father - son 
class person(): #base class
    def __init__(self):
        self.name=""
        self.place=""
        self.job=""
    def display(self):
        print("name",self.name)
        print("place",self.place)
        print("job",self.job)
class student(person):
    def __init__(self):
        self.roll="studetn"
    def display(self):
        print("the person is a student",student)
class teacher(person): # derived from base (person) - teacher- child
    def __init__(self):
        self.id=""
        self.role="teacher"
    # def display(self):
    #     print("role",self.role)
class jobtype(teacher): #private - derived from teacher - private - teacher(base)
    def __init__(self):
        self.job_type=""
    # def display(self):
    #     print(self.job_type)
obj1=jobtype()
obj1.name="aaa"
obj1.job="teacher"
obj1.place="coimbatore"
obj1.id="1234a"
obj1.role="teacher"
obj1.job_type="pivate"
obj1.display()
        
        
#task1
# class
# bank account
# customer 
# account
# transaction 
# methods
# deposit
# with draw
# view balance


 