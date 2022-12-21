import os

def save_key():
    print()
    print("Pretty please read the README first")
    username = input("Enter username: ")
    password = input("Enter password: ")
    filepath = input("Enter path to program file: ")

    with open("./secret/user-key", "w") as fobj:
        fobj.write(username + "\n" + password + "\n" + filepath)
        fobj.close()

if __name__ == '__main__':
    try:
        os.mkdir('./secret/')
    except FileExistsError:
        pass
    save_key()
