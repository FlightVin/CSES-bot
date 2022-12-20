import os

def save_key():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("./secret/user-key", "w") as fobj:
        fobj.write(username + "\n" + password)
        fobj.close()

if __name__ == '__main__':
    try:
        os.mkdir('./secret/')
    except FileExistsError:
        pass
    save_key()
