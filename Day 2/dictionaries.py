# dictionary = A changeable, unordered collection of unique key:values pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}



capitals.update({'Germany': 'Berlin'})  # Adds new key:value pair to dictionary
capitals.update({'USA': 'Las Vegas'})  # Updates the existing key:value pair


capitals.pop('China')  # removes the key:value pair
capitals.clear()  # Removes whole dictionary 


# print(capitals['Germany'])  # To search value in dictionary we need to use key
print(capitals.get('Germany'))  # get is a safer method for searching values, because if value doesnt exist it gives us none, not an error
print(capitals.keys())  # prints all keys in dictionary
print(capitals.values())  # prints all values in dictionary
print(capitals.items())  # prints the whole dictionary

# other way to display a dictionary

# for key, value in capitals.items():
#     print(key, value)