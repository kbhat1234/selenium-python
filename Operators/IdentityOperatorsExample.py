# identity operators (is, is not and in)

a = 10
b = 20
print(a is b)  # False
print(id(a), id(b))  # 1800177713680 1800177714000
print(a is not b)  # True

s1 = 'durga'
s2 = 'durga'
print(s1 is s2)  # True
print(id(s1), id(s2))

str1 = 'Durga'
str2 = 'durga'
print(str1 is str2)  # False
print(id(str1), id(str2))
a1 = 2002.88
a2 = 333.222
print(a1 is not a2)  # True
print(a1 is a2)  # False
print(id(a1), id(a2))  # 2437418109552 2437418112880

l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(f'l1 address is {id(l1)}')  # 2437422371008
print(f'l2 address is {id(l2)}')  # 2437422632256
print(l1 is l2)  # False
print(l1 is not l2)  # True
print(l1 == l2)  # True

l3 = [10, 20, 30, 40, 50]
l4 = [10, 20, 30, 33, 44]
print(f'l3 address is {id(l3)}')  # 2437422633344
print(f'l4 address is {id(l4)}')  # 2437422642176
print(l3 is l4)  # False
print(l3 is not l4)  # True
print(l3 == l4)  # False
