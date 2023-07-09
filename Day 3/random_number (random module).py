import random

x = random.randint(1, 6)  # random int
y = random.random()  # gives us random number between 0 and 1

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)  # gives us random module from list

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)  # randomizes list

print(cards)