a = 11
b = 2
#b = "2.23"
#sum = a + b #TypeError: unsupported operand type(s) for +: 'int' and 'str'
sum = a + b
avg = sum/2
print(f'Sum of {a} and {b} is {sum}')
print(f'Average is {avg}')
print(type(a));print(type(b));print(type(sum));print(type(avg))