a = 20.5
b = 2
print(f'sum of {a} and {b} is {a + b},{type(a + b)}')
print(f'Diff of {a} and {b} is {a - b},{type(a - b)}')
print(f'mul of {a} and {b} is {a * b},{type(a * b)}')
print(f'div of {a} and {b} is {a / b},{type(a / b)}')  # div always result floating point number
print(f'mod of {a} and {b} is {a % b},{type(a % b)}')  # remainder is 0
print(f'exponent of {a} and {b} is {a ** b},{type(a ** b)}')  # 10 to power of 2 is 100
print(
    f'floor division of {a} and {b} is {a // b},{type(a // b)}')  # quotient is 5, it returns integer value if both are
# integer values, else it returns float

# '+' concatenation operator used in string operation
s1 = 'welcome'
s2 = ' karthik'
print(s1 + s2)

# print('welcome '+2376)
'''
print('welcome '+2376)
TypeError: can only concatenate str (not "int") to str
'''

print('welcome ' + '2376')
print('welcome ' + '23.76')
print('welcome ' + str(10))
'''
welcome 10
'''

# '*' repetition operator used in string operations
print('karthik ' * 3)
# print('karthik'*'a')
'''
print('karthik'*'a')
TypeError: can't multiply sequence by non-int of type 'str'
'''
print(4 * 'welcome ')

# print(10/0)
# print(10.8/0)
'''
print(10/0)
ZeroDivisionError: division by zero

print(10.8/0)
ZeroDivisionError: float division by zero
'''

# print(10%0)
# print(10.3%0)
'''
print(10%0)
ZeroDivisionError: integer division or modulo by zero

print(10.3%0)
ZeroDivisionError: float modulo
'''

# print(10//0)
# print(10.72//0)
'''
print(10//0)
ZeroDivisionError: integer division or modulo by zero

print(10.72//0)
ZeroDivisionError: float floor division by zero
'''
