# sort() method = used with lists
# sort() function = used with iterables

# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

# # students.sort(reverse=True)  # works only with lists
# sorted_students = sorted(students, reverse=True)  # students is a tuple

# for i in sorted_students:
#     print(i)

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

# grade = lambda grades:grades[1]  # sorting students by their grades 
age = lambda age:age[2]

# students.sort(key=age)  # sorting students by their age

sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)