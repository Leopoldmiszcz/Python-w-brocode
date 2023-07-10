# class = blueprint to create objects, we can describe attributes, what objects is/has,
# or an objects methods, what each object can do
from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")


car_1.drive()
car_2.stop()
