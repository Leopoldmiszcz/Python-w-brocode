# index operator [] = gives access to a sequence's element (str, list, tuples ect.)

name = "leopold Kaniewski!"

# if(name[0].islower):
#     name = name.capitalize()

first_name = name[:7].upper()
last_name = name[8:].lower()
last_character = name[-1]  # Negative indexing, goes from the back

print(first_name)
print(last_name)
print(last_character)