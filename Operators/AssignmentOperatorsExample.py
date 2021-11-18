a = b = c = d = 10
print(a, "\t", type(a))
print(b, "\t", type(b))
print(c, "\t", type(c))
print(d, "\t", type(d))
print('##################################')
a, b, c, d = 10, 20, 30, 40
print(a, "\t", type(a))
print(b, "\t", type(b))
print(c, "\t", type(c))
print(d, "\t", type(d))

# a,b,c,d=50,60,70
# print(a,b,c,d)
'''
a,b,c,d=50,60,70
ValueError: not enough values to unpack (expected 4, got 3)
'''

# a = 10, b = 20, c = 30, d = 40
# print(f'a is {a}, b is {b}, c is {c}, d is {d}')
'''
a = 10, b = 20, c = 30, d = 40
    ^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
'''

a = 200
b = a
print(f'a is {a}, address is {id(a)}')
print(f'b is {b}, address is {id(b)}')

b += 2

print(f'b is {b}, address after b value is changed {id(b)}')
b += 10
print(f'b is {b}, address after b value is changed {id(b)}')
