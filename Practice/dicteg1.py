info = {"name": "Karthik", "age": 45, "eligible": True, "salary": 20000}
print(info, type(info), id(info))
# {'name': 'Karthik', 'age': 45, 'eligible': True, 'salary': 20000} <class 'dict'> 2359684580160

# Accessing single values
print(info['name'])  # Karthik
print(info.get('eligible'))  # True

# Accessing multiple values
print(info.values())  # dict_values(['Karthik', 45, True, 20000])
print(type(info.values()))  # <class 'dict_values'>

# Accessing keys
print(info.keys())  # dict_keys(['name', 'age', 'eligible', 'salary'])
print(type(info.keys()))  # <class 'dict_keys'>

# Accessing key-value pairs
print(info.items())  # dict_items([('name', 'Karthik'), ('age', 45), ('eligible', True), ('salary', 20000)])
print(type(info.items()))  # <class 'dict_items'>

# adding itmes into dictionary
info['dob'] = "21-Jun-1979"
print(info)  # {'name': 'Karthik', 'age': 45, 'eligible': True, 'salary': 20000, 'dob': '21-Jun-1979'}

# adding/updating the dictionary items using update() method
info = {"name": "Karthik", "age": 46, "eligible": True}
print(info)  # {'name': 'Karthik', 'age': 46, 'eligible': True}
info.update({"age": 47})
info.update({"empno": 670})
print(info)  # {'name': 'Karthik', 'age': 47, 'eligible': True, 'empno': 670}

# removing all items from dictionary using clear() method
info.clear()
print(info)

# removing a particular item using the key in pop() method
info1 = {"name": "Karthik", "age": 45, "eligible": True, "salary": 20000}
info1.pop("eligible")
print(info1)

# removing item using popitem() method
info = {"name": "Karthik", "age": 46, "eligible": True}
info.popitem()
print(info)  # {'name': 'Karthik', 'age': 46}

# removing the item from dictionary using del keyword
info = {"name": "Karthik", "age": 46, "eligible": True}
del info["age"]
print(info)  # {'name': 'Karthik', 'eligible': True}
del info  # deletes entire dictionary with the variable as well
# print(info)  # NameError: name 'info' is not defined. Did you mean: 'info1'?

# copy dictionaries using copy(0 method
info = {"name": "Karthik", "age": 46, "eligible": True, "dob":"21-06-1979"}
new_info = info.copy()
print(f'info -> {info}')  # info -> {'name': 'Karthik', 'age': 46, 'eligible': True, 'dob': '21-06-1979'}
print(f'new_info -> {new_info}')  # new_info -> {'name': 'Karthik', 'age': 46, 'eligible': True, 'dob': '21-06-1979'}

# copy dictionary using dict() method
info = {"name": "Karthik", "age": 46, "eligible": True, "dob":"21-06-1979"}
new_info = dict(info)
print(f'info -> {info}')  # info -> {'name': 'Karthik', 'age': 46, 'eligible': True, 'dob': '21-06-1979'}
print(f'new_info -> {new_info}')  # new_info -> {'name': 'Karthik', 'age': 46, 'eligible': True, 'dob': '21-06-1979'}
