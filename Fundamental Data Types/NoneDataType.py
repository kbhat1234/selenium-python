a = None
b = None
c = None

print(type(a), type(b), type(c))
print(a, b, c)
print(id(a), id(b), id(c))

a = 10
print(id(a))
print(a)
a = None
print(id(a))
print(a)


def f1():
    return 100


def f2():
    print("Hello")


x = f1()
print(x)
print(id(x))

f2()
print(y)
print(id(y))
