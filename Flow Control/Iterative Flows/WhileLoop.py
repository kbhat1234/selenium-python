x = 1
while x <= 10:
    print(x)
    x += 1

n = int(input('Enter some number'))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print(f'sum of first {n} numbers is {s}')

name = ""
pwd = ""
while (name != 'durga') and (pwd != 'python'):
    name = input("Enter Name: ")
    pwd = input("Enter password: ")
print("Hello durga thanks for confirmation")

'''j = 0
while True:
    j+=1
    print("Hello:",j)
'''
for i in range(4):
    for j in range(4):
        print('* ', end='')
    print()