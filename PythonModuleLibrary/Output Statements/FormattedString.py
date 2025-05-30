a, b, c = 10, 20, 30
print("a value is %i" % (a))
print("a value is %i and b value is %i" % (a, b))
print("a value is %i\nb value is %i\nc value is %i" % (a, b, c))

name = 'Karthik'
l = [10, 20, 30, 40]
print(type(l))
print("Hello %s, the list is %s" % (name, l))

# print() using replacement operator {}
name = 'karthik'
salary = 20000
gf = 'sunny'
print('Hello {0} your salary is {1} and your girl friend is {2}'.format(name, salary, gf))
print('Hello {} your salary is {} and your girl friend is {}'.format(name, salary, gf))
print('Hello {x} your salary is {y} and your girl friend is {z}'.format(z=gf, y=salary, x=name))
print(f'name is {name}, your salary is {salary} and girl friend is {gf}')
