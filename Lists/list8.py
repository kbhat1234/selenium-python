l1 = [10, 20, 30, 1, 0]
print(min(l1))
print(max(l1))
print(sorted(l1, reverse=True))
l1.sort(reverse=False)
print(l1)

# lists packing
a = 10
b = 20
c = 30
d = 40
print(a, id(a), type(a))
print(b, id(b), type(b))
print(c, id(c), type(c))
print(d, id(d), type(d))

# lists packing
l = [a, b, c, d]
print(l, id(l), type(l))
print(l[0], id(l[0]), type(l[0]))
print(l[1], id(l[1]), type(l[1]))
print(l[2], id(l[2]), type(l[2]))
print(l[3], id(l[3]), type(l[3]))

# lists unpacking
[a, b, c, d] = l
print(a, id(a), type(a))
print(b, id(b), type(b))
print(c, id(c), type(c))
print(d, id(d), type(d))