# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = "Leopold"  # global scope (available inside & outside functions)

def display_name():
    name = "Kaniewski"  # local scope (available only inside this function), it's used as first
    print(name)

display_name()
print(name)