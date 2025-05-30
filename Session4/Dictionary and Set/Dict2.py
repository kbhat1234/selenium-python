dict1 = {}  # empty dictionary
print(dict1)  # {}

dict1["name"] = "karthik"  # adding "name" with value "karthik" to dict1
dict1["age"] = 45
dict1["Mobile number"] = "9886867677"
dict1["PAN number"] = "AJPPB4129B"
print(dict1)  # {'name': 'karthik', 'age': 45, 'Mobile number': '9886867677', 'PAN number': 'AJPPB4129B'}
print(type(dict1))  # <class 'dict'>

print(dict1["name"])  # karthik
print(type(dict1["age"]))  # <class 'int'>
print(type(dict1["name"]))  # <class 'str'>

dict1["name"] = "Rini"  # overwrite value of "name" key from "karthik" to "rini"
print(dict1)  # {'name': 'Rini', 'age': 45, 'Mobile number': '9886867677', 'PAN number': 'AJPPB4129B'}

dict1["marks"] = [97, 98, 99, 100]
dict1["topics"] = ("python", "c", "java", "javascript")
dict1["id"] = "ID10345"
print(dict1) # {'name': 'Rini', 'age': 45, 'Mobile number': '9886867677', 'PAN number': 'AJPPB4129B', 'marks': [97, 98, 99, 100], 'topics': ('python', 'c', 'java', 'javascript'), 'id': 'ID10345'}

print(dict1["marks"]) # [97, 98, 99, 100]
print(type(dict1["marks"])) # <class 'list'>
print(dict1["topics"]) # ('python', 'c', 'java', 'javascript')
print(type(dict1["topics"])) # <class 'tuple'>

print(dict1["marks"][-1]) # 100
print(dict1["marks"][1:3]) # [98, 99]
print(dict1["topics"][1]) # (c)
print(dict1["topics"][2:]) # ("java", "javascript")

print(dict1.keys())
print(dict1.values())
