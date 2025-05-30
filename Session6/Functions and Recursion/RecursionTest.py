def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)

def showcase(n):
    if (n == 11):
        return
    print(n)
    showcase(n+1)

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n * fact(n-1))


show(5)
showcase(1)
f = fact(0)
print(f'Factorial is {f}')