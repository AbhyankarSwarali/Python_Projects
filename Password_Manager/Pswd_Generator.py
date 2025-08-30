from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("Passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pswd = data.split('|')
            print("Username: ", user)
            print("Password: ", fer.decrypt(pswd.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("Passwords.txt", 'a') as f:
        f.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input("Do you want to add a new password or view the existing passwords? (add/view). Press 'q' to quit: ").lower()
    if mode == 'q':
        break

    if mode == 'view': 
        view()
    elif mode == 'add':
        add()
    else: 
        print("Invalid mode input")
        continue