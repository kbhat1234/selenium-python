class P:
    def m1(self):
        pass


class C(P):
    def m1():
        print("Welcome to child class")
        print("Let's execute some code here")
        s = 10 + 20
        print(f'The sum is {s}')


C.m1()
