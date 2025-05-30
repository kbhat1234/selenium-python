f = open("demo.txt", "r")
data = f.read()
print(data, type(data))
f.close()

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "a+") as f:
    f.write("This is new line")
    data = f.read()
    print(data)

import os
os.remove("demo.txt")