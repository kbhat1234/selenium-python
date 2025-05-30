# tuple packing and tuple unpacking
a = 10
b = 20
c = 30
d = 40
print(a, "->", id(a), type(a), b, "->", id(b), type(b), c, "->", id(c), type(c), d, "->", id(d), type(d))

# packing to tuple
t = a, b, c, d
print(t, id(t), type(t))

print(id(t[0]), type(t[0]), t[0])
print(id(t[1]), type(t[1]), t[1])
print(id(t[2]), type(t[2]), t[2])
print(id(t[3]), type(t[3]), t[3])