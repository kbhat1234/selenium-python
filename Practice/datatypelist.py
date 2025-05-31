# list data type
list = [] # empty list
print(list) # []
list = [2, 6, [3.3, -9, 0.22], ["apple", "banana"], -9.0]
print(list) # [2, 6, [3.3, -9, 0.22], ['apple', 'banana'], -9.0]
print(type(list)) # <class 'list'>
print(id(list)) # 1433866107776
list[2][1] = 6.44
print(list) # [2, 6, [3.3, 6.44, 0.22], ['apple', 'banana'], -9.0]
list[2] = 1
print(list) # [2, 6, 1, ['apple', 'banana'], -9.0]
print(type(list[3][1]))
print(id(list[3][1]))


# tuple data type
tup = () # () empty tuple
print(tup) # ()
print(type(tup)) # <class 'tuple'>
print(id(tup)) # 1801502998640
tup = (("parrot", "sparrow"), ("apple", "banana"))
print(tup) # (('parrot', 'sparrow'), ('apple', 'banana'))
print(type(tup))
print(id(tup))
print(tup[0]) # ('parrot', 'sparrow')
print(tup[1]) # ('apple', 'banana')
print(tup[0][1]) # sparrow
print(tup[1][0]) # apple
print(type(tup[1][0]))
print(id(tup[1][0]))

# range data type range(start, stop, step)

'''
using only stop as 10, start by default as 0 and step counter by default as 1
0
1
2
3
'''
for i in range(4):
    print(i)


