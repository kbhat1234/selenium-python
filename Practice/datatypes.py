a = 10
b = -8
c = 0
print(type(a), type(b), type(c))
print(a, b, c)
cmpl1 = 6 + 15j
cmpl2 = 7 + 10j
sum = cmpl1 + cmpl2
print(cmpl1, type(cmpl1), id(cmpl1))
print(cmpl2, type(cmpl2), id(cmpl2))
print(sum, type(sum), id(sum))

str1 = "hello world !!!"
str2 = "Welcome to world's best programming language"
str3 = str1
print(str1, id(str1), type(str1))
print(str2, id(str2), type(str2))
print(str3, id(str3), type(str3))