text = "Have a nice day! See ya\n"

with open('test.txt', 'a') as file:  # we need that w to write, or we can use append 'a'
    file.write(text)