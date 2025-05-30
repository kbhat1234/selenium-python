s = '0123456789'
print(s)  # 0123456789
print(id(s))  # 3161685195504
print(type(s))  # <class 'str'>

# print(s[::0])  # ValueError: slice step cannot be zero
print(s[0])  # 0
print(s[-1])  # 9
print(s[4])  # 4

print(s[0:])  # 0123456789
print(s[:5])  # 01234
print(s[:])  # 0123456789
print(s[2:6:1])  # 2345

print(s[2:6:-1])  # nothing will print
print(s[-1:-7:1])  # nothing will print

'''
s1 = input("Enter any string: ")
print(len(s1))
print(len(s1.strip()))
print(s1.lstrip())
print(s1.rstrip())
print(s1.rindex('a'))
print(s1.index('a'))

print(s1.find("bhat"))
print(s1.rfind("bhat"))
print(s1.count('unix'))
'''
s2 = "  Welcome to jungle resorts, unix is an operating system, linux is multiuser operating system  "
print("'{}' is s2 ".format(s2))
print(type(s2))
print("Length of s2 before stripping is ", len(s2))

print("String s2 after lstrip is ", s2.lstrip())
print("Length of s2 when strip is from left (lstrip()) is", len(s2.lstrip()))

print("string s2 after rstrip is ", s2.rstrip())
print("Length of s2 when strip is from right (rstrip) is", len(s2.rstrip()))

print("Length of s2 when strip is ", len(s2.strip()))

print(s2.find('o'))\

print(s2.rfind('o'))
print(s2.index('a'))
print(s2.rindex('a'))
print(s2.count('operating'))
print(s2.count('operating',44,88))

s3 = "welcome to python tutorials, enjoy the python coding"
print(s3)
print(id(s3))
print(len(s3))
print(s3.replace('python', 'java'))
print(id(s3.replace('python', 'java')))
print(len(s3.replace('python', 'java')))

s4 = "welcome"
print(s4)
print(id(s4))
s4 = s4.replace('welcome','bye')
print(s4)
print(id(s4))

s = 'Durga Software Solutions PVT Ltd'
print(s)
print(type(s), id(s))
l = s.split()
print(s.split())
print(type(s.split()))
for x in l:
    print(x)

s6 = '21-06-1979'
print(s6)
print(type(s6))
print(id(s6))

l = s6.split('-')
print(l)
print(type(l))
print(id(l))

for y in l:
    print(y)


s7 = '10,20,30,40,50,60,70,80'
l1 = s7.rsplit(',')
print(l1)
print(type(l1))
print(id(l1))

for z in l1:
    print(z)

l = ['durga','software','solutions']
s = '#'.join(l)
print(l)
print(type(l))
print(s)
print(type(s))

t1 = ('durga','soft','solutions')
s1 = '@'.join(t1)
print(t1)
print(type(t1))
print(s1)
print(type(s1))

# changing the case of the string - upper(), lower(), swapcase(), title()
