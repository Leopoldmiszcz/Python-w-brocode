#  while loop = a statement that will execute its block of code,
#  as long as it's condition remains true

name = input("Enter your name: ")

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

