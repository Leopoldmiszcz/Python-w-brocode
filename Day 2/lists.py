# lists = used to store multiple items in a single variable
# u can change elements in lists
food= ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

food.append("ice cream")  # adds something to the end of a list
food.remove("hotdog")  # removes something from a list
food.pop()  # removes last elements in a list
food.insert(0, "cake")  # adds something at a specific index
food.sort()  # sorts list alphabetically
# food.clear()  # removes all elements in a list

print(food[3])

for x in food:
    print(x)