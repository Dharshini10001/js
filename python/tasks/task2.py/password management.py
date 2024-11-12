from cryptography.fernet import Fernet

''' def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file: # wb - write in  bites
        key_file.write(key) '''
        


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.bytes
fer = Fernet(key)

# write_key()


def view():
    try:
        with open("passwords.txt", 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                if not data:  # Skip empty lines
                    continue
                parts = data.split(" | ")
                if len(parts) != 2:  # Ensure there are exactly 2 parts
                    print(f"Skipping malformed line: {data}")
                    continue
                user, password = parts  
                print("User: ", user, " | Password: ", fer.decrypt(password.encode()))           
    except FileNotFoundError:
        print("No passwords found. Please add some passwords first.")

    # with open ("passwords.txt",'r') as f:  # w -only override the file , r - only read the file , you cannot write, a - append the letter in the file.
    #     for line in f.readlines():
    #        data = line.rstrip()
    #        user , passwords = data.split(" | ")  
    #        print("user: ",user , "password: " , passwords)           
         
def add():
    name = input("Account Name: ")
    pwd = input("PAssword: ")
    with open ("passwords.txt",'a') as f:  # w -only override the file , r - only read the file , you cannot write, a - append the letter in the file.
        # f.write(name + " " + pwd + "\n")
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
while True:
    
    mode = input("would you like to add a new password or view existing ones.(view,add) , press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue