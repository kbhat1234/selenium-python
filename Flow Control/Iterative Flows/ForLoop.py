# count the no. of characters in the given string
s = "Karthik Bhat"
print(s)
print(type(s))
count = 0
for x in s:
    count += 1
    print(x)
print("Number of characters in the given string is ", count)
"""
Karthik Bhat
<class 'str'>
K
a
r
t
h
i
k
 
B
h
a
t
Number of characters in the given string is  12
"""

# count the no. of elements in the list
l = [10, 20, 30, 40, 'a', 'A', 10.44]
print(type(l))
print(l)
count = 0
for x in l:
    count += 1
    print(x, end=',')
print("\nThe number of elements in list is ", count)
"""
<class 'list'>
[10, 20, 30, 40, 'a', 'A', 10.44]
10,20,30,40,a,A,10.44,
The number of elements in list is  7
"""

# count no. of elements in the tuple
t = (10, 20, 30, 40)
count = 0
for x in t:
    count += 1
    print(x)
print("The number of elements in tuple is ", count)
"""
10
20
30
40
The number of elements in tuple is  4
"""

# print the characters with the index of the given string
s1 = input("Enter some data ")
i = 0
for x in s1:
    print("The character present at ", i, "is at index ", x)
    i += 1
"""
Enter some data bhat
The character present at  0 is at index  b
The character present at  1 is at index  h
The character present at  2 is at index  a
The character present at  3 is at index  t
"""

# print only characters with the index 1 to end of the given string, not the print the 0th index
s1 = input("Enter some data ")
i = 0
for x in s1:
    if i != 0:
        print("The character present at ", i, "is at index ", x)
    i += 1
"""
Enter some data karthik
The character present at  1 is at index  a
The character present at  2 is at index  r
The character present at  3 is at index  t
The character present at  4 is at index  h
The character present at  5 is at index  i
The character present at  6 is at index  k
"""

# using range() function, print given string 'hello' 3 times
s1 = "Hello"
for x in range(3):
    print(s1)
"""
Hello
Hello
Hello

"""

for x in range(3):
    print('karthik')
"""
karthik
karthik
karthik
"""

# print 0 to 10 when range(11) provided
for x in range(11):
    print(x)
"""
0
1
2
3
4
5
6
7
8
9
10
"""

# print odd numbers when range provided as 0 to 20
for x in range(21):
    if x % 2 != 0:
        print(x)
"""
1
3
5
7
9
11
13
15
17
19
"""

# print even numbers when range provided as range(0,40,2)
for x in range(0, 40, 2):
    print(x)
"""
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
"""

# print odd numbers when range provide as range(1,40,2)
for x in range(1, 40, 2):
    print(x)
"""
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
"""

# print reverse range(10,0,-1)
for x in range(10, 0, -1):
    print(x)
"""
10
9
8
7
6
5
4
3
2
1
"""

# sum of numbers in the list
li = eval(input("Enter any data "))
s = 0
for x in li:
    s += x
print(type(s))
print("The sum of the numbers is ", s)
"""
Enter any data [10,20,30,33]
<class 'int'>
The sum of the numbers is  93
"""
