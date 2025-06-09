# Remove() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
# cities.remove("XYZ") # KeyError: 'XYZ'
# print(cities)

# discard() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo")
print(cities)
cities.discard("XYZ")
print(cities)

# remove item from set using pop() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(f'item {item} is removed from set')  # item Tokyo is removed from set
print(cities)

# remove the entire set using del keyword
# del cities
# print(cities)  # NameError: name 'cities' is not defined

# remove items from set without deleting the variable using clear() method
cities.clear()
print(cities)  # set()

cities = {"Mumbai", "Delhi", "Kolkata", "Chennai", "Bangalore", "Hyderabad"}
if "Bangalore" in cities:
    print(f'Mumbai is present in set {cities}')
else:
    print(f'Mumbai is not present in set {cities}')

if "Paris" not in cities:
    print(f'Paris not present in set {cities}')
else:
    print(f'Paris is present in set {cities}')
