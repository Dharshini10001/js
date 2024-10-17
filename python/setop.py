# 2 methods
# set()
# {}
# unorder - collections 
#we cant access index values 
# myset=set(("1","2","3"))
# print(myset)
# print(type(myset))

# myset1={"one","two","three"}
# print(type(myset1))
# print(myset1)
# set operations
# union
# intersection
# difference
# ^
myset1={1,2,3,4,5,6}
myset2={1,2,3,7,8,9,"cat","dog","birds"}
# union |
print(myset1|myset2)
# differnce - 
print(myset2-myset1)
# intersections &
print(myset1&myset2)
# ^ skip common values - symmentric difference
print(myset1^myset2)
# set methos ()
# add
# remove
# discord
# pop
myset1.add(7)
print(myset1)
myset1.remove(1)
print(myset1)
myset1.discard(2)
print(myset1)
items=myset1.pop()
print(items)
print(myset1)

mylist=list(myset1)
print(mylist)
print(type(mylist))

for i in myset2:
    print(i)
    
number=[1,2,3,4,5,6,7,8,9]
i=0
while i < number:
    print(i)
    i=i-1