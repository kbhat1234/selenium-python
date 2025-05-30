# ternary operator
a = False
b = False
x = True if a > b else False
print(x)

x = "10 is lesser" if (30 < 20) else 40
print(x)

a, b = 10, 20
x = "Greater" if a > b else "Smaller"
print(f'Value of x is {x}')

# reading data from keyboard
a = int(input("Enter a "))
b = int(input("Enter b "))
min_value = a if a < b else b
print(f'Min value {a} and {b} is {min_value}')

p = int(input("Enter 1st number: "))
q = int(input("Enter 2nd number: "))
r = int(input("Enter 3rd number: "))

max_value = p if (p > q and p > r) else q if (q > r and q > p) else r
print(f'Max value {p},{q},{r} is {max_value}')

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
print("both numbers are equal" if a == b else "1st number is greater than second number" if a > b else
"1st number is smaller than second number")
