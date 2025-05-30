t = (10, 20, 'a', 'b')
l1 = []
print(type(l1))
print(l1)
l1.append('karthik')
print(l1)
print(l1.index('karthik'))

l2 = [10, 20, 30, 40]
print(l2)

l3 = [10, 20, [30, 40], 50, 60]
print(type(l3))
print(l3[2][0])

l4 = eval(input("Enter any input:"))
print(type(l4), l4)

l5 = list(l3)
print(type(l5), l5)

l6 = list(t)
print(type(l6), l6)

s = "karthik k bhat"
l7 = s.split(' ')
print(type(l7), l7)
# l3 = [10, 20, [30, 40], 50, 60]
print(l3[0])
print(l3[3])
print(l3[:])
print(l3[2:])
print(l3[:2])
print(l3[-1])
print(l3[-3])
print(l3[2][0])
print(l3[2][1])