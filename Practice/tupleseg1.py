tuple1 = (1, 2, 8, 4, 2, 5, 6, 9)
tuple2 = ("Red", "Green", "Blue", "Yellow")
print(tuple1)  # (1, 2, 8, 4, 2, 5, 6, 9)
print(type(tuple1), id(tuple1))
print(tuple2)  # ('Red', 'Green', 'Blue', 'Yellow')
print(type(tuple2), id(tuple2))

details = ("Karthik Bhat", 45, 'BTECH CSE', 9.6)
print(details)  # ('Karthik Bhat', 45, 'BTECH CSE', 9.6)
print(type(details), id(details))
print(type(details[0]), type(details[3]))

# positive indexing - [0], [1], [2], ...
country = ("Spain", "Italy", "India", "England", "Germany")
print(country, type(country), id(country))
print(country[3])  # England
print(country[1])  # Italy
# print(country[9]) # IndexError: tuple index out of range

# negative indexing - [-5], [-4], [-3]....
print(country[-1])  # Germany
print(country[-4])  # Italy

# check for item
if "India" in country:
    print("India in country tuple")
else:
    print("India not in country tuple")

if "Russia" in country:
    print("Russia in country tuple")
else:
    print("Russia not in country tuple")

# Range of index - range(start:end:jump index)
# Print elements within a particular range
animals = ("cat", "dog", "bat", "mouse", "pig", "horse")
print(animals[1:4])  # ('dog', 'bat', 'mouse')
print(animals[-4:-2])  # ('bat', 'mouse')

# printing all elements from a given index till end
print(animals[2:])  # ('bat', 'mouse', 'pig', 'horse')
print(animals[-3:])  # ('mouse', 'pig', 'horse')

# printing all elements from start to given end index
print(animals[:3])  # ('cat', 'dog', 'bat')
print(animals[:-4])  # ('cat', 'dog)

# printing alternate values
print(animals[::2])  # ('cat', 'bat', 'pig')
