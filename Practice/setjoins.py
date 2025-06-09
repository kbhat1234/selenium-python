# using union() method - returns  the new set
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.union(cities2)
print(cities3)  # {'Delhi', 'Berlin', 'Seoul', 'Madrid', 'Tokyo', 'Kabul'}

# using update() method - adds items to the existing set from another set
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.update(cities2)
print(cities1)  # {'Delhi', 'Berlin', 'Seoul', 'Madrid', 'Tokyo', 'Kabul'}

# using intersection() method
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.intersection(cities2)
print(cities3)  # {'Tokyo', 'Madrid'}

# using intersection_update() method
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.intersection_update(cities2)
print(cities1)  # {'Tokyo', 'Madrid'}

# using symmetric_difference() method
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)  # {'Berlin', 'Seoul', 'Kabul', 'Delhi'}

# using symmetric_difference_update() method
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.symmetric_difference_update(cities2)
print(cities1)  # {'Kabul', 'Delhi', 'Berlin', 'Seoul'}

# using difference() method
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.difference(cities2)
print(cities3)  # {'Berlin', 'Delhi'}

# using difference_update() method
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities1.difference_update(cities2)
print(cities1)  # {'Delhi', 'Berlin'}
