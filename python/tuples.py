# tuple used store multiple values in single variable
# tuple()
# list [] - when list(())
# list changeable but tuple is immutable not change
# list and tuples both are and accessing using index values , and supoorts more datatyples ,dublicate values
# creating tuples
my_tuple=("one","two", 3, 5, 4,4)
print(my_tuple)
print(type(my_tuple))
print(type(my_tuple[1]))
print(type(my_tuple[3]))

# accessing tuples

print(my_tuple[1])
print(my_tuple[1:5]) #skips index[5] item becoz it takes start index [0]
print(my_tuple[:5])
print(my_tuple[1:])
print(my_tuple[:])

# length of tuples
print(len(my_tuple))

# creating tuples using constructor
 
my_tup=tuple(("apple","orange","banana"))
print(my_tup)

# memebership operator

if "orange" in my_tup:
    print("orange is one of tuple items ")

# update tuple items - directly we cant change tuple items but converts tuple to list - list to tuple

ConList=list(my_tup)
ConList[2]="kiwi"
my_tup=tuple(ConList)
print(my_tup)

ConList=list(my_tup)
ConList[2]="melon"
my_tup=tuple(ConList)
print(my_tup)
# adding items in tuple
ConList=list(my_tup)
ConList.append("grapes")
my_tup=tuple(ConList)
print(my_tup)

ConList=list(my_tup)
ConList.append("blackcurrent")
my_tup=tuple(ConList)
print(my_tup)

# 2 method

add_tupe=("orange",)
my_tuple+=add_tupe
print(my_tuple)

con_tup=("one","two","three","four","five")
add_tup=("Six",)
con_tup+=add_tup
print(con_tup)
# remove method
ConList=list(my_tup)
ConList.remove("apple")
my_tup=tuple(ConList)
print("remove tuple values:",my_tup)
# delete
# del my_tup
# print(my_tup)

# unpacking tuples

new_tup=("apple","two","three")
(one,two,three)=new_tup
# print(one)

new_tup=("apple","two","fruits")
(one,two,three)=new_tup
print(one)
print(three)


new_tuple2=(1,2,8,9,3,4,5,6,7)
print(min(new_tuple2))
print(max(new_tuple2))
print(sorted(new_tuple2))
print(reversed(new_tuple2))
# new_tuple2.sort(reverse=True)
print(new_tuple2)
print(any(new_tuple2))
print(all(new_tuple2))
# print(count(new_tuple2))
print(sum(new_tuple2))
# thistuple=()
a=("one","two",'three')
print(max(a))
# b=[1,7,9,0,"one","two",'three','four','eight',"yock"]
# print(max(b))
tuple=("orange","apple","Banana","grapes","melon","Lemon","cherry")
print(tuple[-1])
print(tuple[2:3])
print(tuple[:2])
print(tuple[2:])
print(tuple[2:-2])
if "orange" in tuple:
    print("yes")
else:
    print("no")
#  join the tuple
tuple1=("one","two","three","four","five","six")    
tuple2=("Seven","Eight","nine","ten")
tuple3=tuple1 + tuple2
print(tuple3)
tuple4=("orange","apple","melon","palm","watermelon")
tuple5=tuple4*2
print(tuple5)
thistuples=("orange","apple","melon","palm","watermelon","one","two","three","four","five","six")
for i in thistuples:
    print(i)
for i in range(len(thistuples)):
    print(thistuples[i])
i=0
while i<len(thistuples):
    print(thistuples[i])
    i=i+1
