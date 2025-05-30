l1 = []
for x in range(1,11):
    l1.append((x*2)*0)
print(l1)

l2 = [x*x for x in range(1,11)]
print(l2)

l3 = [x for x in range(1,21) if x%2 ==0]
print(l3)

l4 = [x*x for x in range(1,11)]
l5 = [x for x in l4 if x%2!=0]

print(l4)
print(l5)

l6 = [x**2 for x in range(1,21) if (x**2)%2!=0]
print(l6)

words = ['Balaiah', 'Nag', 'Venkatesh', 'Chiru']
l = [w[0] for w in words]
print(l)

ll1 = [w for w in words if len(w)>6]
print(ll1)

n1 = [10, 20, 30, 40]
n2 = [30, 40, 50, 60]
n3 = [n for n in n1 if n not in n2]
print(n3)
n4 = [n for n in n2 if n not in n1]
print(n4)

words = "the quick brown fox jumps over the lazy dog".split()
print(words)

l = [[w.upper(), len(w)] for w in words]
print(l)

tup = (10, 20, 30, 40)
print(tup)
lis = list(tup)
print(lis)