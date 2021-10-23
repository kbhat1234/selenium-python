r = range(10)
print(f'range is {r}, and range type is {type(r)}')
for x in r:
    print(f'x value is {x}')

r1 = range(100)
print(f'range us {r1}, and range type is {type(r1)}')

for x in r1:
    print(f'x value is {x}')

r2 = range(1,10)
print(f'range is {r2}, and range type is {type(r2)}')

for x in r2:
    print(f'x value is {x}')

r3 = range(1,11)
print(f'range is {r3}, and range type is {type(r3)}')

for x in r3:
    print(f'x value is {x}')

r4 = range(1,11,1)
print(f'range is {r4}, and range type is {type(r4)}')

for x in r4:
    print(f'x value is {x}')

r5 = range(1,50,5)
print(f'range is {r5}, and range type is {type(r5)}')

for x in r5:
    print(f'x value  is {x}')

r6 = range(50,1,-5)
print(f'range is {r6}, and range type is {type(r6)}')

for x in r6:
    print(f'x value is {x}')

r7 = range(23,43)
print(f'x value is {r7[4]}')
print(f'x value is {r7[-1]}')

r = r7[5:10]
for x in r:
    print(f'x value is {x}')
