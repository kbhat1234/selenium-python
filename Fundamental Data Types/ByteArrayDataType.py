l1 = [10,20,40,30]
ba1 = bytearray(l1)
print(l1)
print(type(ba1))

for x in ba1:
    print(x)
'''
[10, 20, 40, 30]
<class 'bytearray'>
'''

l2 = [10,33,44,22,10,255]
ba2 = bytearray(l2)
print(l2)
print(type(ba2))

for x in ba2:
    print(x)
'''
[10, 33, 44, 22, 10, 255]
<class 'bytearray'>
10
33
44
22
10
255
'''

# l3 = [10,44,55,256]
# ba3 = bytearray(l3)
# print(l3)
# print(type(ba3))

# for x in ba3:
#    print(x)
'''
Traceback (most recent call last):
  File "C:\\Users\\kbhat.anurag\\PycharmProjects\\pythonlearning\\ByteArrayDataType.py", line 32, in <module>
    ba3 = bytearray(l3)
ValueError: byte must be in range(0, 256)
'''

l4 = [10,44,55,255]
ba4 = bytearray(l4)
print(l4)
print(type(ba4))

for x in ba4:
    print(x)

print(ba4[2])
print(ba4[-1])
ba4[2] = 43
for x in ba4:
    print(x)

r = ba4[2:]
for x in r:
    print(x)  
