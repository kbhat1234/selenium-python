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