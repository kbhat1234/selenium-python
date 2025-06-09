# string method - upper()
str1 = "welcome to python programming !!!"
print(len(str1))
print(str1.upper()) # WELCOME TO PYTHON PROGRAMMING

# string method - lower()
print(str1.lower()) # welcome to python programming

# string method - strip()
print(str1.strip()) # Welcome to python programming

# string method - rstrip()
print(str1.rstrip("!")) #Welcome to python programming

# String method - replace()
str2 = "Mango Banana Orange Pineapple"
print(str2.replace("Moon", "Spoon"))
print(str2.replace("M", "Sp"))

# string method - split()
print(str2.split(" "))
print(type(str2.split(" ")))

# string method - capitalize()
str3 = "python is Easy and secured Programming laNguage"
print(str3.capitalize())

# string method - center()
print(str3.center(100,"*"))

# string method - count()
print(str3.count("n"))

# string method - endswith()
st1 = "Welcome to python programming"
print(st1.endswith("ing")) # True
print(st1.endswith("program")) # False
print(st1.endswith("mm", 18, 28))
print(len(st1))

# string method - find()
st2 = "He's name is Dan. He is an honest man"
print(st2.find("Daniel")) # return -1 on no search found
print(st2.find("Dan")) # returns index 13

# string method - isalnum()
st3 = "Welocmetoconsole"
print(st3.isalnum()) # True

st4 = "Welcome to console"
print(st4.isalnum()) # False

st5 = "Welcome123"
print(st5.isalnum()) # True

st6 = "Welcome123!!!"
print(st6.isalnum()) # False

# string method - isalpha()
t1 = "I'm 18 years old"
print(t1.isalpha()) # False

t2 = "Hello !!!!"
print(t2.isalpha()) # False

t3 = "Hello"
print(t3.isalpha()) # True

# string method - islower()
st6 = "welcome to python programming"
print(st6.islower()) # True

st7 = "Welcome to python Programming"
print(st7.islower()) # False

st8 = "Hurray @@###"
print(st8.islower()) # False