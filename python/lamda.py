# it is a anonymous function
# function name - only arguments
# used to declare anonymous - lambda
# varname = lambda argumemnt : expersion
multiple = lambda x:x+2
print(multiple(5))

def multply(a,b):
    return lambda x,y:x+y*b
local=multply(10,20)
print(local(10,30))