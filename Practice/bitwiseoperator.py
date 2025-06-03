x = 16
if (x > 15):
    print(f'x is greater than 15')
else:
    print(f'x is not greater than 15')
print(f'Value of x is {x}')

# None
print("None: ", bool(None))

# Numbers
print("Zero: ", bool(0))
print("One: ", bool(1))
print("Integer: ", bool(23))
print("Float: ", bool(2.34))
print("Complex: ", bool(2+4j))

# Strings
print("Any string: ", bool("Welcome"))
print("String containing number: ", bool("23.88"))
print("Empty String: ", "")

# lists
print("List: ", bool([10, 20, 3.5]))
print("Empty list: ", bool([]))

# tuple
print("Tuple: ", bool((10, 'a', 2.4)))
print("Empty tuple: ", bool(()))

# dictionary
print("Empty dictionary: ", bool({}))
print("Dictionary :", bool({"name" : "Karthik", "age" : 45}))

# sets
print("Empty sets: ", bool(set()))
print("Set: ", bool({10, "karthik", 22, 10}))

# membership operators
a = [2, 4, 6, 1, 9, 7]
search = 1
if (search in a):
    print(f'{search} present in list a')
else:
    print(f'{search} not present in list a')
print(f'list is {a}')

srch = 20
if(srch not in a):
    print(f'{srch} is not present in list a')
else:
    print(f'{srch} is present in list a')
print(f'list is {a}')

# identity operator
s1 = 20
s2 = 20
if(s1 is s2):
    print(f's1 is same as s2')
else:
    print(f's1 is not s2')
print(f'{s1} is s1 \n{s2} is s2')

if(s1 is not s2):
    print(f's1 is not same as s2')
else:
    print(f's1 is same as s2')
print(f'{s1} is s1 \n{s2} is s2')

# logical operators
p1 = 10; p2 = 20; p3 = 5
if(p1 > p2 and p1 > p3):
    print("p1 is greater")
elif (p2 > p1 and p2 > p3):
    print("p2 is greater")
else:
    print("p3 is greater")
print("End of the program")