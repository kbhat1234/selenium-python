import keyword
from random import randint as r

a = 10;
print(type(a));

a = "karthik";
a = 20.22;
print(type(a));

a = 20.22;
print(type(a));

print(r(0, 6), r(3, 6), r(2, 5), r(0, 3), r(1, 4), r(0, 4), sep='');

for i in range(10):
    print(r(0, 9), r(0, 9), r(0, 9), r(0, 9), r(0, 9), r(0, 9), sep='');

print(len(keyword.kwlist));
print(keyword.kwlist);
print(keyword.iskeyword('switch'));
