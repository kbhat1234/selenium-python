name = input("Enter name: ")
if name == 'Karthik' or name == 'karthik':
    print(f'Hello {name}, Good morning')
print('how are you')

brand = input("Enter the favourite brand: ")
if brand == 'RC':
    print(f'It is Royal Challenge brand {brand}')
elif brand == 'KF':
    print(f'It is Kingfisher brand {brand}')
elif brand == 'KO':
    print(f'It is KO brand {brand}')
elif brand == 'FO':
    print(f'It is Fosters brand {brand}')
else:
    print(f'{brand} brand is not supported')
print('thank you')

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print("The num1 value is %i " % num1)
print("The num2 value is %i " % num2)

# biggest of 2 numbers
if num1 > num2:
    print(f'{num1} is greater than {num2}')
elif num2 > num1:
    print(f'{num2} is greater than {num1}')
else:
    print(f'{num1} and {num2} are equal')

# biggest of 3 numbers
num1 = eval(input("Enter 1st number: "))
num2 = eval(input("Enter 2nd number: "))
num3 = eval(input("Enter 3rd number: "))

print("The num1 value is %i " % num1)
print("The num2 value is %i " % num2)
print("The num3 value is %i " % num3)

if num1 > num2 and num1 > num3:
    print('Biggest number is ', num1)
elif num2 > num3 and num2 > num1:
    print('Biggest number is ', num2)
elif num3 > num1 and num3 > num2:
    print('Biggest number is ', num3)
else:
    print('All numbers are equal')

# entered number is even or odd
n = eval(input("Enter any number: "))
if n % 2 == 0:
    print(f'entered number {n} is even')
else:
    print(f'entered number {n} is odd')

# entered number is in between 1 and 100
n = int(input("Enter any number: "))

if n >= 1 and n <= 100:
    print("The number ", n, "is in between 1 and 100")
else:
    print("The number ", n, "is not between 1 and 100")

num3 = int(input("Enter the digit between 0 to 9: "))
if num3 == 0:
    print("ZERO")
elif num3 == 1:
    print("ONE")
elif num3 == 2:
    print("TWO")
elif num3 == 3:
    print("THREE")
elif num3 == 4:
    print("FOUR")
elif num3 == 5:
    print("FIVE")
elif num3 == 6:
    print("SIX")
elif num3 == 7:
    print("SEVEN")
elif num3 == 8:
    print("EIGHT")
elif num3 == 9:
    print("NINE")
else:
    print("Invalid input digit")
