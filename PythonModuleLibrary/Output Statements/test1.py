print('welcome to python')
print('This is easy programming language')
print('Hello')
print()
print('Good Evening')
print()
print('how are you')
print('Hello\n Good morning\n\twelcome to python')

print('durga'+'software')  # durgasoftware
print('durga'*3)  # durgadurgadurga
print('durga '*3)  # durga durga durga
print('durga '+'software')  # durga software
print('durga'+' software')  # durga software
print('durga','software')  # durga software

a, b, c = 10, 20, 30  # a=10 b=20 c=30
print("The values are ", a, b, c)  # The values are 10 20 30

a, b = 10, 20
c = 12.33
print("The values are ", a, b, c)
print(a, b, c, sep=',')
print(a, b, c, sep=':')


print('Hello', end=' ')
print('Students')
print('Python')
print('Very easy')
"""
Hello Students
Python
Very easy
"""

print('Hello', end=' ')
print('Students', end=' ')
print('Python', end=' ')
print('Very easy', end=' ')
"""
Hello Students Python Very easy
"""

print(10, 20, 30, sep=',', end='...')
print(40, 50, 60, sep=':')

list = [10,20,30,40]
tuple = (10,20,30,40)
set = {2,4,3,2}

print(list,end='...')
print(tuple,end='...')
print(set)
print(list, tuple, set)