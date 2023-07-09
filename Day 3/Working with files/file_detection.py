import os

path = "C:\\Users\\leopo\\OneDrive\\Pulpit\\Korok.txt"  # We need double backslashes!!!

if os.path.exists(path):
    print("That location exists!")
else:
    print("That location doesn't exist!")
