str1 = "Welcome to python"
print(len(str1))
print(len("welcome"))
print(str1[0])
print(str1[-1])
print(str1[1:4])
print(str1[1:])
print(str1[:4])
print(str1[:])

# \'
str2 = "welcome to 'python' programming"
print(str2)

#\"
str3 = 'welcome to "python" programming'
print(str3)

# \\
str4 = "Hello \\world"
print(str4)

# \n
str5 = "Welcome to \nPython \nProgramming"
print(str5)
print(str3.upper())
print(str3.lower())
print(str3.title())
print(str3.strip())
print(str3.find("python"))
print(str3.replace("python","java"))
print("pro" in str3)
print("pro" not in str3)