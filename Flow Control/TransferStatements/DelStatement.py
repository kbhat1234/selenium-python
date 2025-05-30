x = 10
print(x)
print(id(x))
# del x
# print(x)

name = "karthik"
print(name)
print(id(name))
del name, x
# print(name)

s1 = "karthik"
print(s1)
print(id(s1))
s1 = None
print(s1)
print(id(s1))
s1 = "rini"
print(s1)
print(id(s1))
s1 = None
print(s1)
print(id(s1))

s2 = 'karthik'
s3 = 'karthik'
s4 = 'karthik'
print(id(s2))
print(id(s3))
print(id(s4))

del s2
print(id(s3), id(s4))
print(s3, s4)