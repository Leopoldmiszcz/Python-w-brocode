# tuple = collection which is order and unchangeable
#         used to groud together related data

student = ("Leopold", 14, "male")

print(student.count("Leopold"))  # counts how many times that value appeared in a tuple
print(student.index("male"))  # shows in which index/indexes that value is

for x in student:
    print(x)

if "Leopold" in student:
    print("Leopold is here")
