str1 = "7"
str2 = "3.145"
str3 = "13"
num1 = 10
num2 = 6.67

print(int(str1), type(int(str1)), id(int(str1))) # 7 <class 'int'> 2395197342128
print(float(str2), type(float(str2)), id(float(str2))) # 3.145 <class 'float'> 2395198380688
print(float(str3), type(float(str3)), id(float(str3))) # 13.0 <class 'float'> 3070098134960
print(str(num1), type(str(num1)), id(str(num1))) # 10 <class 'str'> 1935978535920
print(str(num2), type(str(num2)), id(str(num2))) # 6.67 <class 'str'> 1935978535920