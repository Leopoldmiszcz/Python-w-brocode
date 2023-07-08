# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}


# utensils.add("napkin")  # adds something to set
# utensils.remove("fork")  # removes something from set
# utensils.clear()  # clears the set
# dishes.update(utensils)  # adds set to set

print(dishes.difference(utensils))  # displays differences between two sets
print(utensils.intersection(dishes))  # displays common values with in two sets

dinner_table = utensils.union(dishes)  # creates a new set from utensils and dishes

for x in dinner_table:
    print(x)