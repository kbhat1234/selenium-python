tup = (2, 1, 3, 1)
print(type(tup))
print(tup)
print(tup[0])

# tup[1] = 6 # TypeError: 'tuple' object does not support item assignment
tup1 = (1,)
print(tup1); print(type(tup1))
print(tup[1:3])

# tup.index(1) # returns first occurrence of value 1
print(tup.index(2))
# print(tup.index(22)) #ValueError: tuple.index(x): x not in tuple

count = tup.count(1) # counts total occurrences
print(count)