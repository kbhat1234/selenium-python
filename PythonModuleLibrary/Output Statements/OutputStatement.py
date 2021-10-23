print()
print('how are you')
print('karthik' + ' bhat')
print('karthik ' * 3)
print("durga", "software")

a, b, c = 10, 20, 30
print("the values are: ", a, b, c, sep=',')

l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
s = {10, 20, 30, 40}

print(l, end='...')
print(t, end='...')
print(s)

name = input("Enter the name: ")
if name == 'durga':
    print(f'Hello {name}, good morning!!! how are you')
else:
    print(f'Good luck')

brand = input("Enter the favourite brand: ")
if brand == 'RC':
    print(f'It is Royal Challenge brand {brand}')
elif brand=='KF':
    print(f'It is Kingfisher brand {brand}')
elif brand =='KO':
    print(f'It is KO brand {brand}')
elif brand=='FO':
    print(f'It is Fosters brand {brand}')
else:
    print(f'{brand} brand is not supported')

print("End of the program")

