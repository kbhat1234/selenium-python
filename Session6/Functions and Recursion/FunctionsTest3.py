def func1(a, b=2):
    return a * b

def func2(a=10, b= 30):
    mul = a * b
    print(f'Product of {a} and {b} is {mul}')


mul = func1(10)
print(f'product is {mul}')

func2()
func2(100)
func2(9)