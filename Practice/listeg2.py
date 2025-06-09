# change list items
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Karthik" # item 'Nadia' is replaced by "Karthik'
print(names) #  ['Harry', 'Sarah', 'Karthik', 'Oleg', 'Steve']

names[2:4] = ["Rini", "Kaustubh"]
print(names) # ['Harry', 'Sarah', 'Rini', 'Kaustubh', 'Steve']

names[1:4] = ["Karthik", "Ishani"]
print(names) # ['Harry', 'Karthik', 'Ishani', 'Steve']

names[2:4] = ["Rahul", "Vijay", "Manju", 'Ajay', "kinder"]
print(names) # ['Harry', 'Karthik', 'Rahul', 'Vijay', 'Manju', 'Ajay', 'kinder']