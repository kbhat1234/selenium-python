# list data type
list = [] # empty list
print(list) # []
list = [2, 6, [3.3, -9, 0.22], ["apple", "banana"], -9.0]
print(list) # [2, 6, [3.3, -9, 0.22], ['apple', 'banana'], -9.0]
print(type(list)) # <class 'list'>
print(id(list)) # 1433866107776
list[2][1] = 6.44
print(list) # [2, 6, [3.3, 6.44, 0.22], ['apple', 'banana'], -9.0]
list[2] = 1
print(list) # [2, 6, 1, ['apple', 'banana'], -9.0]
print(type(list[3][1]))
print(id(list[3][1]))


# tuple data type
tup = () # () empty tuple
print(tup) # ()
print(type(tup)) # <class 'tuple'>
print(id(tup)) # 1801502998640
tup = (("parrot", "sparrow"), ("apple", "banana"))
print(tup) # (('parrot', 'sparrow'), ('apple', 'banana'))
print(type(tup))
print(id(tup))
print(tup[0]) # ('parrot', 'sparrow')
print(tup[1]) # ('apple', 'banana')
print(tup[0][1]) # sparrow
print(tup[1][0]) # apple
print(type(tup[1][0]))
print(id(tup[1][0]))

# range data type range(start, stop, step)

'''
using only stop as 10, start by default as 0 and step counter by default as 1
0
1
2
3
'''
for i in range(4):
    print(i)

# using start and stop
for i in range(0, 20):
    print(i)

# using start, stop and step
for i in range(2, 20, 2):
    print(i)

# using negative step
for i in range(20, 2, -2):
    print(i)

# dictionary
dict = {}
print(dict, type(dict), id(dict))
dict = {
    "name" : "karthik",
    "age" : 45,
    "canvote" : True
}
print(dict) # {'name': 'karthik', 'age': 45, 'canvote': True} 
print(type(dict)) # <class 'dict'> 
print(id(dict)) # 1536752894208
print(dict["name"]) # karthik

fruits = {
    "name" : ["orange", "banana", "litchi", "mango"],
    "quantity": [4, 12, 25, 10]
}
print(fruits) # {'name': ['orange', 'banana', 'litchi', 'mango'], 'quantity': [4, 12, 25, 10]}
print(fruits["name"]) # ['orange', 'banana', 'litchi', 'mango']
print(fruits["quantity"]) # [4, 12, 25, 10]
keys = fruits.keys() 
values = fruits.values()
print(keys) # dict_keys(['name', 'quantity'])
print(values) # dict_values([['orange', 'banana', 'litchi', 'mango'], [4, 12, 25, 10]])
print(fruits["name"][0])  # orange
print(type(fruits["name"][0])) # <class 'str'>
print(fruits["quantity"][0]) # 4
print(type(fruits["quantity"][0])) # <class 'int'>
print(type(keys), type(values)) # <class 'dict_keys'> <class 'dict_values'>

# binary data - converting string to bytes
str1 = "Welcome to python programming"
arr1 = bytes(str1, 'utf-8')
print(arr1) # b'Welcome to python programming'
print(type(arr1)) # <class 'bytes'>
arr2 = bytes(str1, 'utf-16')
print(arr2) # b'\xff\xfeT\x00h\x00i\x00s\x00 \x00i\x00s\x00 \x00a\x00 \x00s\x00e\x00c\x00o\x00n\x00d\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'
print(type(arr2)) # <class 'bytes'>

# creating bytes of given size
b = bytes(4)
print(b) # b'\x00\x00\x00\x00'
print(type(b)) # <class 'bytes'>

# bytearray() - converting string to bytes
str1 = "This is first string"
arr1 = bytearray(str1, 'utf-8')
print(arr1) # bytearray(b'This is first string')
print(type(arr1)) # <class 'bytearray'>
print(id(arr1)) # 2348638639344

arr2 = bytearray(str2, 'utf-16')
print(arr2) # bytearray(b'\xff\xfeT\x00h\x00i\x00s\x00 \x00i\x00s\x00 \x00a\x00 \x00s\x00e\x00c\x00o\x00n\x00d\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00')
print(type(arr2)) # <class 'bytearray'>
print(id(arr2)) # 2348638639088

# creating bytes of the given size using bytearray()
b = bytearray(5)
print(b) # bytearray(b'\x00\x00\x00\x00\x00')