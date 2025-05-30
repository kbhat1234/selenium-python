l1 = [20, 30, 20, 10, 15, 6, 8, 6, 10]
print("The length of list is ", len(l1))

print("Count of 20 is ", l1.count(20))

# if object is not in list
print(l1.count(200))

print("index of 10 is (1st occurrence)  ", l1.index(10))

#  ValueError: 101 is not in list
#  print("index of 10 is (1st occurrence)  ", l1.index(101))

target = int(input("Enter the value to search:"))
if target in l1:
    print(target, "is available and its first occurence is at:", l1.index(target))
else:
    print(target," not available")

l1.append(200)
print(l1)

l2 = []
for x in range(101):
    if x%10 == 0:
        l2.append(x)
print(l2)

l3 = []
for x in range(0, 101, 10):
    l3.append(x)
print(l3)

l3.insert(2, 20)
print(l3)
l3.insert(50, 99)
l3.insert(-44, 33)
print(l3)

l4 = [10, 20, 30]
l5 = [7, 0, 22, 3, 22, 44]
l4.extend(l5)
print(l4)
print(l5)
l5.sort(reverse=True)
print(l5)

l4.clear()
print(l4)
l4 = l5.copy()
print(id(l4), id(l5))
print(l4)
l4.remove(7)
print(l4)
l4.pop(-5)
print(l4)
print(l1+l2)
l1.reverse()
print(l1)

l7 = l1
print(l7, id(l7), l1, id(l1))
l1.append(33)
print(l7, id(l7), l1, id(l1))
l1.clear()
print(l1, l7)
