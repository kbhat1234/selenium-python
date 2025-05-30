s = input("Enter any string: ")
n = len(s)
i = 0
print("Printing string in forward direction")
while i < n:
    print(s[i], end='')
    i += 1
print()

i = -1
print("printing string in reverse direction")
while i >= -n:
    print(s[i], end='')
    i -= 1
print()
