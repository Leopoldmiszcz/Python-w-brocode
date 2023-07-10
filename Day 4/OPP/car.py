class Car:  # class = blueprint of an object

    def __init__(self, make, model, year, color):  # __init__ is a constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color


    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")
