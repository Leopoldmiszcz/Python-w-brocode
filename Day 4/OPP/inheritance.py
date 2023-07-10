class Animal:  # Parent class

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):  # Child class
    def run(self):
        print("This rabbit is running")
class Fish(Animal):  # Child class
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):  # Child class
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(Rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()