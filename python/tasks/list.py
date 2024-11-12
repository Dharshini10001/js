new_list=list((4,8,9,2,0,1,3,5,7,6))
print(new_list)
first=int(input("Enter the options number:"))
new_list.sort()
sorted=new_list
print(sorted)
new_list.sort(reverse = True)
reversed=new_list
print(reversed)
if first ==1:
    second=int(input("Enter the index value:"))
    print(sorted[second])
elif first ==2:
    delete=int(input("Enter the index value you want delete:"))
    sorted.pop(delete)
    print(delete)
    print(new_list)
elif first ==3:
    insert= int(input("Enter the value you want insert:"))
    sorted.append(insert)
    new_list.sort()
    print(insert)
    print(new_list)
elif first ==5:
    values_list = []
    while True:
        user_input = input("Enter a value (or type 'q' to quit): ")
    
        if user_input == 'q':
            break
        else:
            try:
                value = int(user_input)
                values_list.append(value)
            except ValueError:
                print("Invalid input! Please enter a valid integer or 'q' to quit.")
    print(values_list)
    soer_new=new_list+values_list
    soer_new.sort()
    print(soer_new)   
    
    
else:
    print("Invalid option! Please enter a number between 1 and 5.")
