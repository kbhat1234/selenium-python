# lists
list1 = [10, 20, 3, 5, 6, 5]
list2 = ["Karthik", 46, "BTECHCSE", 9.3]
print(list1, type(list1), id(list1)) # [10, 20, 3, 5, 6, 5] <class 'list'> 2127149679296
print(list2, type(list2), id(list2)) # ['Karthik', 46, 'BTECHCSE', 9.3] <class 'list'> 2127149694208

# positive indexing [0], [1], [2], etc...
print(list1[4], type(list1[4])) # 6 <class 'int'>

# negative indexing [-1], [-2], [-3], etc...
print(list2[-4], type(list2[-4])) # Karthik <class 'str'>

# check for item in list
color = ["Yellow", "Red", "Pink", "Green", "Blue"]
if "Pink" in color:
    print("Pink color in list")
else:
    print("Pink color not in list")

# range of index range(start:end:jumpindex]
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey"]
print(animals[3:6]) # ['mouse', 'pig', 'horse']
print(animals[:3]) # ['cat', 'dog', 'bat']
print(animals[-6:-3]) # ['dog', 'bat', 'mouse']
print(animals[3:]) # ['mouse', 'pig', 'horse', 'donkey']
print(animals[-6:]) # ['dog', 'bat', 'mouse', 'pig', 'horse', 'donkey']
print(animals[::]) # ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse', 'donkey']
print(animals[:-1]) # ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']

print(animals[:6]) # ['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
print(animals[:-4]) # ['cat', 'dog', 'bat']

# printing alternate values
print(animals[::2]) #['cat', 'bat', 'pig', 'donkey']
print(animals[-6:-2:2]) # ['dog', 'mouse']

# printing 3rd consecutive values
print(animals[0:6:3]) # ['cat', 'mouse']

# add items to list using append()
colors = ["yellow", "blue", "green"]
print(colors) # ['yellow', 'blue', 'green']
colors.append("red")
print(colors) # ['yellow', 'blue', 'green', 'red']

# add items to list using insert()
colors.insert(1, "pink")
print(colors) # ['yellow', 'pink', 'blue', 'green', 'red']

# add items to the list using extend()
rainbow = ["viloet", "purple", "orange"]
colors.extend(rainbow)
print(colors) # ['yellow', 'pink', 'blue', 'green', 'red', 'viloet', 'purple', 'orange']