#if statement = a block of code that will execute if it's condition is true
age = int(input("How old are you: "))

if age >= 18: #If one if is true the other elif and else will not be used
    print("You are an adult!")
elif age == 100:
    print("You are a century old!")
elif age < 0: #elif is a combination of else and if
    print("You haven't been born yet!")
else:
    print("You are a child!")
