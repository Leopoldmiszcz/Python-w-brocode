# walrus operator :=

# new to python 3.8
# assignment expression aka walrus
# assigns values to variables as part of a larger expression

# foods = list()
# while True:
#   food = input("What a food do you like: " )
#   if food == "quit":
#     break
#   foods.append(food)


foods = list()

while food := input("What food do you like?: ") != "quit":
    foods.append(food)
