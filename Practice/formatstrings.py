# format strings
name = "Karthik"
age = 45
statement = "My name is {} and my age is {}"
print(f'My name is {name} and my age is {age}')
print(statement.format(name, age))

# format the string using index
quantity = 2
fruit = "Apples"
cost = 120.0
statement = "I want to buy {2} of {0} for {1}$"
print(statement.format(fruit, cost, quantity))

print(f'My name is {name} and my age is {age}')