# unpacking of tuple
t = (10, 20, 30, 40)
print(t, id(t), type(t))
print(t[0], id(t[0]), type(t[0]))
print(t[1], id(t[1]), type(t[1]))
print(t[2], id(t[2]), type(t[2]))
print(t[3], id(t[3]), type(t[3]))

a, b, c, d = t
print(a, "->", id(a), type(a))
print(b, "->", id(b), type(b))
print(c, "->", id(c), type(c))
print(d, "->", id(d), type(d))