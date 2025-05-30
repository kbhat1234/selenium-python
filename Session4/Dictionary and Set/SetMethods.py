set1 = set()
set1.add(1)
set1.add(2)
set1.add(2)
print(set1); print(type(set1))
set1.remove(2)
# set1.remove(8) # KeyError: 8
print(set1)
set1.add(4)
set1.add(7)
print(set1)
set1.add("karthik")
set1.add(("rini", "ishani"))
print(set1)

list = [1, 2, 3, 4, 5]
# set1.add(list) # TypeError: unhashable type: 'list'

dic = {
    "name" : "karthik",
    "age" : 44
}
# set1.add(dic) # TypeError: unhashable type: 'dict'
# print(set1)
# set1.clear()
# print(set1) # set() will clear the collection set1

set1.pop()
set1.pop()
print(set1)
