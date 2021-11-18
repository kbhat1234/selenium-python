l1 = [10, 20, 30, 40]
l2 = [22, 'durga', 20.44, 'karthik', True, 0b1011, 0o22, 0x20]
l3 = [10, 20, 30, 40]
l4 = l3

print(f'list l1 is {l1}, list type is {type(l1)}, and list address is {id(l1)}')
print(f'list l2 is {l2}, list type is {type(l2)}, and list address is {id(l2)}')
print(f'list l3 is {l3}. list type is {type(l3)}, and list address is {id(l3)}')
print(l3)
print(l4)
print(id(l3), id(l4))
l1[0] = 50
print(l1)
l2[1] = 'kali'
print(l2)

l = []
print(l)
l.append(10);
l.append(20);
l.append(30);
l.append(40);
print(l)
l.remove(30)
print(l)
