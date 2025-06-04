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
# add list to list
rainbow = ["violet", "purple", "orange"]
colors.extend(rainbow)
print(colors) # ['yellow', 'pink', 'blue', 'green', 'red', 'violet', 'purple', 'orange']

# add tuple to list
car = ["ford", "vw", "skoda", "suzuki"]
car1 = ("mercedes", "fiat", "jeep")
car.extend(car1) # ['yellow', 'pink', 'blue', 'green', 'red', 'violet', 'purple', 'orange']
print(car) # ['ford', 'vw', 'skoda', 'suzuki', 'mercedes', 'fiat', 'jeep']
print(car1) # ('mercedes', 'fiat', 'jeep')

# add set to list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = {"Mercedes", "Volkswagen", "BMW"}
cars.extend(cars2)
print(car)  # ['ford', 'vw', 'skoda', 'suzuki', 'mercedes', 'fiat', 'jeep']
print(cars) # ['Hyundai', 'Tata', 'Mahindra', 'BMW', 'Volkswagen', 'Mercedes']
cars.extend(car)
print(cars)
print(car)

#add dictionary to list
students = ["Sakshi", "Aaditya", "Ritika"]
students2 = {"Yash": 18, "Devika": 19, "Soham": 19}
students.extend(students2)
print(students) # ['Sakshi', 'Aaditya', 'Ritika', 'Yash', 'Devika', 'Soham']

# remove items from list - pop() without providing the index
colors = ["Red", "Yellow", "Green", "Blue", "Pink"]
colors.pop() # last item in the list will be deleted
print(colors) # ['Red', 'Yellow', 'Green', 'Blue']

# pop() giving the index
colors.pop(2) # "Green" is removed from index 2
print(colors) # ['Red', 'Yellow', 'Blue']

# remove() with providing the item to be deleted
colors.remove("Yellow") # item "Yellow" will be removed from the list
print(colors) # ['Red', 'Blue']

colors.append("Violet")
colors.append("Orange")
print(colors)

# del a particular item from list providing the specified index
del colors[1] # item "Blue" will be removed from the list at index 1
print(colors) # ['Red', 'Violet', 'Orange']

# del the entire list and variable itself
# del colors # entire list items deleted with variable colors
# print(colors) # NameError: name 'colors' is not defined

# clear() list items - empty list
colors.clear() # empty the list
print(colors) # []
