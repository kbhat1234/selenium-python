s = 'karthikbhat'
print(s[0])
print(s[10])
# print(s[11])  #IndexError: string index out of range
print(s[7])
print(s[-1])
print(s[-3])
print(s[:])
print(s[2:])
print(s[:5])
print(s[2:6])

s = input("Enter any string: ")
i = 0
for x in s:
    print("The character present at positive index {} and at negative index {} is : {}".format(i, i - len(s), x))
    i += 1

str1 = "Welcome to jungle"
print(str1[0:7])  # Welcome
print(str1[4:9])  # ome t
print(str1[3:])  # come to jungle
print(str1[:5])  # Welco
print(str1[0])
print(str1[-2])

# str1[begin:end:step]
print(str1[:])  # Welcome to Jungle
print(str1[::])  # default step would be 1
print(str1[3:9:1])  # come t
print(str1[3:9:2])  # cm
print(str1[3:9:3])  # ce
print(str1[::-1])  # elgnuj ot emocleW

print(str1[-1:-7:1])  #
print(str1[0:7:1])
