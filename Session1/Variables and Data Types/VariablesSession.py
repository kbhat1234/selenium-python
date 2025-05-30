name = "KARTHIK" #string
age = 45 #integer
price = 25.99 #float
id_no = None

print(f'My name is {name}, \nage is {age}, \nPrice is {price}, \nId no is {id_no}')
print("\n")
print(f'{name} is of type {type(name)}, \n{age} is of {type(age)}, \n{price} is of type {type(price)}, \n{id_no} is of type {type(id_no)}')

is_selected = True
print (type(is_selected))

num1 =  float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
sum = num1 + num2
print(f'Sum of {num1} and {num2} numbers is {round(sum)}')