x = 10
print(f'value of x is {x}')
print(f'address of x is {id(x)}')

x = x+1
print(f'after change value of x is {x}')
print(f'after change the address of x is {id(x)}')


a = 10
b = a
print(f'value of a is {a} and address of a is {id(a)}')
print(f'value of b is {b} and address of b is {id(b)}')

b = b + 1
print(f'value of a is {a} and address of a is {id(a)}')
print(f'value of b is {b} and address of b is {id(b)}')

p = 10
q = 10
r = 10
print(f'value of p is {p} and address is {id(p)}')
print(f'value of q is {q} and address is {id(q)}')
print(f'value of r is {r} and address is {id(r)}')

print(p is q);

a = True
b = True
print(a is b)

a = 10+20j
b = 10+20j
print(a is b)
print(id(a))
print(id(b))
