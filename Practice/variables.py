a = 10; print(a, type(a))
b = 20; print(b, type(b))
c = a; print(c, type(c))
str1 = "Welcome to python programming world's"; print(str1, type(str1))
f = 10.23; print(f, type(f))
is_check = True; print(is_check, type(is_check))

list = [10, 'a', "apple", 20.1,True]
tup = (10, 'a', "apple", 20.33, False)
print(list, type(list), id(list)); print(tup, type(tup), id(tup))
print(id(a)); print(id(b)); print(id(c))

if ((id(a) == id(c))):
    print("both variables pointing to same memory location")
else:
    print("both are pointing to different memory location")

l2 = list
print(l2, type(l2), id(l2))

param1 = 20
param2 = 10.33
sum = param1 + param2
print(f'Sum of {param1} and {param2} is {sum}')
print(type(sum), id(sum))

div = param1/param2
print(div, type(div), id(div))

none = None
print(none, type(none), id(none))

none = 67
print(none, type(none), id(none))

print(3, type(3), id(3))