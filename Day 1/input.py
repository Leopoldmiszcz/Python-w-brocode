name = input("What is your name?: ") #Input gets us string type
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age += 1

print("Hello " + name)
print("You are " + str(age) + " years old")
print("You are " + str(height) + "cm tall")