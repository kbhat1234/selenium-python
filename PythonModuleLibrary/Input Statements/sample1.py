"""
x = input("Enter something: ")
print(type(x))
print(x)
y = int(x)
print(y)
print(type(y))

# read 2 numbers from keyboard and print sum of 2 numbers
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
sum = x + y
print("The sum is ", sum)

print('The sum is ', int(input('Enter 1st number: ')) + int(input('Enter 2nd number: ')))

a, b = [int(x) for x in input("Enter any 2 numbers: ").split()]
print('The sum is ', a + b)

x, y, z = [int(p) for p in input("enter any 3 numbers: ").split()]
print(f'The sum is {x+y+z}')

x, y, z = [int(p) for p in input("enter any 3 numbers: ").split(':')]
print(f'The sum is {x+y+z}')
"""

a, b = [float(x) for x in input("Enter any 2 float values: ").split(',')]
print('The sum is ', a + b)

