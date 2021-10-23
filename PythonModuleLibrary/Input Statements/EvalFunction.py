x = eval("10+20+30")
print(x, type(x))

ex = input("Enter some expression: ")
result = eval(ex)
print(result, type(result), type(ex))

ex1 = eval(input("enter some expression: "))
print(type(ex1))
print(ex1)
for x1 in ex1:
    print(x1)

a, b = [eval(x) for x in input("Enter 2 values: ").split(None)]
add = a + b
print(f'type of {a} is {type(a)}, type of {b} is {type(b)}')
print(f'The sum is {add}')