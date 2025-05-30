set = set()
tup =  (2,3,2,5)
set.add(22)
set.add(33)
set.add(44)
set.add(22)
set.add(21)
set.add("karthik")
set.add(tup)
print(set); print(type(set)); print(len(set))
set1 = set.copy()
print(set1)
set2 = set.copy()
print(set2)

union = set1.union(set2)
print(union)

intersec = set1.intersection(set2)
print(intersec)

set3 = {2, 4, 5, 6, 3, 2, 3}
set4 = {10, 11, 2, 4, 2, 8, 9}
print(set3, type(set3), len(set3))
print(set4, type(set4), len(set4))

un = set3.union(set4) # un = set3.union(set4) # {2, 3, 4, 5, 6, 8, 9, 10, 11}
print(un, type(un), len(un)) # {2, 3, 4, 5, 6, 8, 9, 10, 11} <class 'set'> 9

inter = set3.intersection(set4) # {2, 4}
print(inter, type(inter), len(inter)) # {2, 4} <class 'set'> 2