# str.format = optional method that gives users
#              more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)

# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {1}".format(animal, item))  # positional argument
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))  # keyword argument

# text = "The {} over the {}"
# print(text.format(animal, item))

# Padding

# name = "Leopold"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {name:10}. Nice to meet you!".format(name))  # adding padding
# print("Hello, my name is {:<10}. Nice to meet you!".format(name))  # adding padding left
# print("Hello, my name is {:>10}. Nice to meet you!".format(name))  # adding padding right
# print("Hello, my name is {:^10}. Nice to meet you!".format(name))  # adding padding center


# Format numbers

number = 1000
print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))  # binary
print("The number is {:o}".format(number))  # octal
print("The number is {:x}".format(number))  # hexadecimal
print("The number is {:e}".format(number))  # scientific notation
