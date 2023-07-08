# logical operators (and, or, not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):  # and operator; both conditions must be true
    print("The temperature is bad today!")
    print("Stay inside!")


elif not(temp < 0 or temp > 30):  # or operator; one of the conditions must be true
    print("The temperature is good today!")
    print("Go outside!")

# not operator flips true to false and false to true

