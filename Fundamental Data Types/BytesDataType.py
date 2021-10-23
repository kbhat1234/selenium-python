l1 = [10,20,30,40,244,255]
b1 = bytes(l1)
print(l1)
print(type(b1))

print(b1[0])
print(b1[-1])

r = b1[1:4]
for x in r:
    print(x)

for x in b1:
    print(x)
'''
[10, 20, 30, 40, 244, 255] <class 'bytes'>
10
20
30
40
244
255
'''

# l2 = [10,20,30,40,244,256]
# b2 = bytes(l2)
# print(l2, type(b2))
# for x in b2:
#    print(x)
'''
Traceback (most recent call last):
  File "C:\\Users\\kbhat.anurag\\PycharmProjects\\pythonlearning\\BytesDataType.py", line 8, in <module>
    b2 = bytes(l2)
ValueError: bytes must be in range(0, 256)
'''

# b[0] = 44
# for x in b:
#    print(x)
'''
Traceback (most recent call last):
  File "C:\\Users\\kbhat.anurag\\PycharmProjects\\pythonlearning\\BytesDataType.py", line 8, in <module>
    b[0] = 44
TypeError: 'bytes' object does not support item assignment
'''