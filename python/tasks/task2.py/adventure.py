name = input("Type your name:")
print("Welcome ", name ,"To this adventure game!")

answer= input("you are in a dirt road, it has come to an end and you can go left or right. Which way would you like to go ? ").lower()


if answer == "left":
    answer = input("you come to a river , you can walk around it or swim accross? Type walk to walk around and swim to swim accross:")
    
    if answer =="swim":
        print("You swam accross and were eaten by an alligator .")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. you lose")
        
        
elif answer == "right":
    answer=input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)")
    
    if answer == "back":
        print("you go back and lose.") 
    if answer == "cross":
        answer=input("you cross the bridge and meet a stranger. Do you talk to them (Yes/ No)")

        if answer =="yes":
            print("you talk to the stranger and they are give Gold!")
        elif answer =="no":
            print("you ignore the stranger and they are offended and you lose .")
        else:
            print("Not a valid option. you lose.")
            
else:
    print("Not a valid option. you lose.")
    
    
    
