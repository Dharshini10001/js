# array
# array - strore collections data but same type 
# integer - integer
# array datatype - module - array
# module - collection of functions
# import array - create array
# ary_var_name=array.array(datatype,[1,2,3,4])
#integer - i - it accepts both positive and negative number , I- only positive numbers
#float - f - float
#string - u -unicode
import array
array_name=array.array('I',[1,2,3,4,5,6])
print(array_name)
for i in array_name:
    print(i)
print(array_name[3])
import array as ar
array2=ar.array('f',[1,2,3,4,5,6,-1.0,1.3])
print(array2)
from array import *
# *- all methods()
array3=array('u',['h','e','l','l','o'])
print(array3)
# using pop()
array3.pop(2)#index value
print(array3)
array3.insert(1,'h')
print(array3)