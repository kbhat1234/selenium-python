x = [10, 20, [30, 40]]
x.remove(20)
print(x)
x[1].remove(40)
x[1].remove(30)
print(x)

y = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(y)

print("Elements Row Wise:")
for r in y:
    print(r)

print("Elements in Matrix style:")
for m in range(len(y)):
    for n in range(len(y[m])):
        print(y[m][n], end=' ')
    print()
