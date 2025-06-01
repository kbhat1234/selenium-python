# converting integer to float using float()
a = 10
b = 4.99
c = 2+3j

flt1 = float(a)
print(a, type(a), id(a)) # 10 <class 'int'> 2266472251920
print(flt1, type(flt1), id(flt1)) # 10.0 <class 'float'> 2266473290096

# converting integer to complex using complex()
cmplx1 = complex(a)
print(a, type(a), id(a)) # 10 <class 'int'> 2266472251920
print(cmplx1, type(cmplx1), id(cmplx1)) # (10+0j) <class 'complex'> 2266473289648

# converting float to integer using int()
int1 = int(b)
print(int1, type(int1), id(int1)) # 4 <class 'int'> 2340873765200

# converting float to complex using complex()
cmplx2 = complex(b)
print(cmplx2, type(cmplx2), id(cmplx2)) # (4.99+0j) <class 'complex'> 1969101723568

# converting from complex to integer using complex() - cannot be done
# int2 = int(c)
# print(int2, type(int2), id(int2)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
