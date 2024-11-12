print("Welcome to my computer quiz!")

playing = input("do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's Play Game :)")
score =0

answer = input("What does CPU stands for? ")
if answer.lower() == "center processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
    
answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does DBMS stands for? ")
if answer.lower() == "database management structure":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does DSA stands for? ")
if answer.lower() == "data science and algorithms":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does pdf stands for? ")
if answer.lower() == "protable document file":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What is the use of computer ")
if answer.lower() == "communicate with machine":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What your Mobile OS?")
if answer.lower()  == ("andriod" or "i phone"):
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("you got"  + str(score) +  "questions correct out of 8")