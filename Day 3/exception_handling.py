# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divine: "))
    denominator = int(input("Input a number to divine by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("U can't divine by zero! idiot!")

except ValueError as e:
    print(e)
    print("Enter only numbers plz")

except Exception as e:  # e displays error
    print(e)
    print("Something went wrong!")
else:
    print(result)
finally:  # finally will always execute
    print("This will always execute")