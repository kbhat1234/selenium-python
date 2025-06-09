info = {"carla", 19, False, 5.9, 19}
print(type(info))
print(id(info))
print(info)

# Accessing set items
for item in info:
    print(item)
'''
False
19
5.9
carla
'''

cities = {"Delhi", "Kolkata", "Mumbai", "Bangalore"}
cities2 = {"Bangalore", "Hyderabad", "Lucknow", "Mumbai"}
# cities.update(cities2)
print(cities)
print(cities2)
# cities.update(list(cities2))
# cities.update(tuple(cities2))
# cities.update(dict(cities2))
cities.update(set(cities2))
print(cities)