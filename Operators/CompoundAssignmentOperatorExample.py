# compound assignment operator

a = 100
print(f'value of a is {a}, address of a is {id(a)}')
a += 10  # a = a + 10
print(f'value of a after change is {a}, address of a is {id(a)}')
print('#########################################################')

b = 10
print(f'value of b is {b}, address of b is {id(b)}')
b -= 5  # b = b - 10
print(f'value of b after change is {b}, address of b is {id(b)}')
print('#########################################################')

c = 200
print(f'value of c is {c}, address of c is {id(c)}')
c *= 5  # c = c * 5
print(f'value of c after change is {c}, address of c is {id(c)}')
print('#########################################################')

d = 25
print(f'value of d is {d}, address of d is {id(d)}')
d /= 5  # d = d / 5
print(f'value of d after change is {d}, address of d is {id(d)}')
print('#########################################################')

a1 = 25
print(f'value of a1 is {a1}, address of a1 is {id(a1)}')
a1 //= 5  # a1 = a1 / 5
print(f'value of a1 after change is {a1}, address of a1 is {id(a1)}')
print('#########################################################')

a2 = 25
print(f'value of a2 is {a2}, address of a2 is {id(a2)}')
a2 %= 5  # a2 = a2 % 5
print(f'value of a2 after change is {a2}, address of a2 is {id(a2)}')
print('#########################################################')

a3 = 8
print(f'value of a3 is {a3}, address of a3 is {id(a3)}')
a3 **= 5  # a3 = a3 ** 5
print(f'value of a3 after change is {a3}, address of a3 is {id(a3)}')
print('#########################################################')

b1 = 25
print(f'value of b1 is {b1}, address of b1 is {id(b1)}')
b1 &= 5  # b1 = b1 & 5
print(f'value of b1 after change is {b1}, address of b1 is {id(b1)}')
print('#########################################################')

b2 = 25
print(f'value of b2 is {b2}, address of b2 is {id(b2)}')
b2 |= 5  # b2 = b2 | 5
print(f'value of b2 after change is {b2}, address of b2 is {id(b2)}')
print('#########################################################')

b3 = 25
print(f'value of b3 is {b3}, address of b3 is {id(b3)}')
b3 ^= 5  # b3 = b3 ^ 5
print(f'value of b3 after change is {b3}, address of b3 is {id(b3)}')
print('#########################################################')
