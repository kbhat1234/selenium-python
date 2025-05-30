emp_no = int(input("Enter employee number: "))
emp_name = input("Enter employee name: ")
emp_sal = float(input("Enter employee salary: "))
emp_addr = input("Enter employee address: ")
emp_married = bool(input("Enter employee married: "))

print(f'employee number type is {type(emp_no)}')
print(f'employee name type is {type(emp_name)}')
print(f'employee salary type is {type(emp_sal)}')
print(f'employee address type is {type(emp_addr)}')
print(f'Employee married or not?: {type(emp_married)}')

print(f'employee number is {emp_no}')
print(f'employee name is {emp_name}')
print(f'employee salary is {emp_sal}')
print(f'employee address is {emp_addr}')
print(f'employee married is {emp_married}')

a, b = [int(x) for x in input("Enter 2 numbers: ").split()]  # split() by default takes 2 arguments with space
print(f'sum is {a + b}')

# Read 2 float values from keyboard which are specified with',' seperation and print sum
p, q = [float(y) for y in input("Enter any 2 float values: ").split(',')]  # split(',')
print(f'The product is {p * q}')

# using eval() function
x = input("Enter any expression: ")
print(type(x))
result = eval(x)
print(result)

x = input("enter some data: ")
print(type(x))
result = eval(x)
print(type(result))
print(f'output is {result}')
for x1 in result:
    print(x1)

x = eval(input("Enter some data: "))
print(f'type of x is {type(x)}')
print(f'output of x is {x}')
for x1 in x:
    print(x1)
