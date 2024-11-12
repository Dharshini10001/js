mylist=['mango', 'grapes', 'papaya', 'kiwi']

def myFunc(x):
	if 'a' in x:
    		return False
	else:
    		return True

filter_var = filter(myFunc, mylist)

for x in filter_var:
  print(x)
