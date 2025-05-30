def greet():
    print("Hello")
    print("Welcome on board")


def greet1(fname, lname):
    print(f"Hello {fname} {lname}")
    print("Welcome on board")


def multiply(*numbers):
    print(numbers)


def func1(number, by=1):
    result = number + by
    print(result)


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("KARTHIK")
print(message)

file = open("context.txt", "w")
file.write(message)
file.close()
file = open("context.txt", "r")
mess = file.read()
print(mess)

'''func1(2)
multiply(2, 3, 4, 5)
greet()
greet1("Karthik", "Bhat")
greet1("Rini Das", "Bhat")
'''
