cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

# using add() method
cities.add("Kolkata")
print(cities)  # {'Madrid', 'Tokyo', 'Berlin', 'Delhi', 'Kolkata'}

# using update() method if you want to add multiple items in set
cities.update({"Mumbai", "Bangalore"})
print(cities)  # {'Delhi', 'Bangalore', 'Tokyo', 'Madrid', 'Berlin', 'Mumbai', 'Kolkata'}

# passing the list to set
cities2 = ["Chennai", "Jaipur", "Gurgaon"]
cities.update(cities2)
print(cities)  # {'Kolkata', 'Tokyo', 'Madrid', 'Delhi', 'Jaipur', 'Mumbai', 'Chennai', 'Bangalore', 'Gurgaon',
# 'Berlin'}

# passing the tuple to set
cities2 = ("Paris", "London")
cities.update(cities2)
print(cities)  # {'Paris', 'Kolkata', 'Tokyo', 'London', 'Madrid', 'Delhi', 'Jaipur', 'Mumbai', 'Chennai',
# 'Bangalore', 'Gurgaon', 'Berlin'}

# passing the dictionary to set
cities2 = {"city": "Agartala", "pin": 562149}
cities.update(cities2)
print(cities)  # {'Bangalore', 'Delhi', 'Berlin', 'Chennai', 'pin', 'Gurgaon', 'Madrid', 'Paris', 'city', 'Tokyo',
# 'Mumbai', 'Jaipur', 'London', 'Kolkata'}
