# isdisjoint() method - checks if items of a give set are present in another set. Returns False if the items present,
# else return False
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities1.isdisjoint(cities2))  # False

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities1.isdisjoint(cities2))  # True

# issuperset() method - checks if all items of a particular set are present in the original set. It returns True if
# all items are present, else return False
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities1.issuperset(cities2))  # False
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities1.issuperset(cities3))  # False

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities1.issuperset(cities2))  # True

# issubset() method - checks if all the items of the original set are present in particular set. It returns True if
# all items present, else it returns False
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities1))  # True

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities2.issubset(cities1))  # False
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities3.issubset(cities1))  # False



