student = {
    "name" : "Karthik",
    "id" : "ID878788",
    "subjects" : {
        "physics" : 98,
        "chemistry" : 99,
        "maths" : 100,
        "biology" : 98
    },
    "topics" : {
        "1" : ("java", "javascript", "python", "c"),
        "2" : ("devops", "ai", "ml", "data science")
    },
    "age" : 45,
    "class" : "12th"
}
print(student, type(student))
print(student["name"], type(student["name"]))

print(student["subjects"], type(student["subjects"]))
print(student["subjects"]["maths"], type(student["subjects"]["maths"]))
print(student["topics"]["2"][1:3], type(student["topics"]["2"][1:3]))