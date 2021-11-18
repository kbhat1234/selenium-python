if True:
    pass
else:
    print("it is false")


def f1():
    print("function 1")


def f2():
    pass
    # print("Hi")


def f3():
    f2()
    # f1()


f3()

for i in range(1, 100):
    if i % 10 == 0:
        print(i)
    else:
        pass
