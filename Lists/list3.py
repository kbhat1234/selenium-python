lis = ["A", "B", "C", "D"]
x = len(lis)
for i in range(x):
    print(lis[i], "is available at positive index ", i, "and at negative index ", i-x)


def f1():
    print("This is function f1()")


def f2():
    print("This is function f2()")


class Test:
    def test1(self):
        print("This is the class method test1()")


f1()
s = Test()
s.test1()
f2()