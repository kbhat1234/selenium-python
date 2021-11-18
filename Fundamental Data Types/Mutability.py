l = [10, 20, 30, 40]
print(l)
print(id(l))
l[0] = 74
print(l)
print(id(l))

l1 = [10, 20, 30, 40]
l2 = l1
print(l1)
print(l2)
l1[0] = 40
print(l1)
print(l2)
l2[1] = 30
print(l1)
print(l2)
