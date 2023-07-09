import os

path = "C:\\Users\\leopo\\OneDrive\\Pulpit"  # We need double backslashes!!!

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a dircetory!")
else:
    print("That location doesn't exist!")
