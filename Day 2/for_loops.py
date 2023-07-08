import time

# for loop = a statement that will execute its block of code
# a limited amount of times
#
# while loop = unlimited
# for loop = limited

# for i in range(10):
#     print(i+1)

# for i in range(50, 100):  # 50 is a starting number inclusive and 100 is an ending number exclusive
#     print(i)

# for i in range(50, 100+1, 2):  # it iterates every second (iteruje się co drugi)
#     print(i)

# for i in "Leopold":
#     print(i)

for seconds in range(10, 0, -1): # -1 makes the countdown goes backwards
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
