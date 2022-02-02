t = ()
lis = ['a','b','c','d']
st = "this is string"
dic = {'name': 'karthik', 'id': 999333}

print(t, type(t))
t = (10,)
print(t)
print(id(t))
t = (10, 20, 30, 40)
print(t)
print(id(t))
t = tuple(dic)
print(t)
print(id(t))
t = ('karthik', 20, 'rini', 'ishani', 40, 'kaustubh', 10, 20, 22, 25)
print(t)
print(id(t))
print(len(t))
print(t.count(20))
print(t.index(10))

t= (23, 10, 3, 4, 5, 24, 88)
print(t, type(t))
l = sorted(t)
print(l, type(l))

t1 = (20, 1, 2, 4, 3, 10)
print(t1)
print(id(t1))
t2 = sorted(t1, reverse=True)
print(t2)
t3 = tuple(t2)
print(t3)
print(id(t3))
print(min(t3), max(t3))

