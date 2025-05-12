dic = {
    "name" : "karthik",
    "age" : 45,
    "address" : "bangalore"
}

keys = dic.keys()
values = dic.values()
print(keys, values)
print(len(dic))
print(list(dic.keys()))
#print(dic["age1"]) # KeyError: 'age1' if invalid key provided, then we get key error.
print(dic.items()) # ([('name', 'karthik'), ('age', 45), ('address', 'bangalore')])
print(dic.get("age1")) # if invalid key provided then the output will show as None.

dic1 = {
    "pincode" : "576101",
    "Mobile" : "9886867677"
}

dic.update([dic1])
print(dic)
