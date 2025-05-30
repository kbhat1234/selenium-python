dict = {
    "name" : "apna college",
    "subjects" : ["python", "C", "java"],
    "topics" : ("dict", "sets"),
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
}

print(dict)
print(dict["name"]); print(dict["subjects"])
print(dict["subjects"][1])

dict1 = {"name" : "Karthik",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "math" : 95
    }
}

print(dict1)
print(dict1["score"]["math"])
dict1["score"]["bio"] = 100
print(dict1)
