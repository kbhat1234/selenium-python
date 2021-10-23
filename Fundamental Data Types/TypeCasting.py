# type casting float to int, complex to int, bool to int, str to int

print(int(10));
print(int(0b1011));
print(int(0o234));
print(int(0x1234));

print(int(10.33));

# print(int(10+20j)); # Type error

print(int(True));
print(int(False));

# print(int('abcd')); # Type error
print(int('10'));

# print(int('10.22')); # Value error
# print(int('0b1011')); # value error
# print(int('0o23')); # value error
# print(int('0x15')); # value error

print(int(0b1011));
print(int(0o232));
print(int(0x212));

# type casting float to int, float to complex float to bool, float to str
print(float(10.0012));
print(float(10));
print(float(0b1011));
print(float(0o7));
print(float(0x32));

# print(float(10+20j)); # type error

print(float(True));
print(float(False));

# print(float('karthik')); # value error
print(float('12'));
print(float('12.33'));


# type casting complex to int, complex to float, complex to bool, complex to str
print(complex(10)); # 10+0j
print(complex(2.33)); # 1.33+0j
print(complex(10,20)); # 10+20j
print(complex(0.2,2.3)); # 0.2+2.3j
print(complex(2.2j));
print(complex(True)); # 1+0j
print(complex(False)); # 0j
print(complex('12'));
print(complex('12.33'));
# print(complex('10','20'));
# print(complex(10,'13'));
# print(complex('karthik')); # value error

print(bool(10));
print(bool(0));

print(bool(0.0));
print(bool(0.001));
print(bool(1.23));

print(bool(0+0j));
print(bool(1+0j));
print(bool(0+1j));
print(bool(1.1+0j));

print(bool('True'));
print(bool('False'));
print(bool('yes'));
print(bool('no'));
print(bool(''));

print(str(12));
print(str(0b101011));
print(str(0o23));
print(str(0x54));

print(str(12.22));
print(str(10+20j));
print(str(1.2+2.1j));

print(str(True));
print(str(False));
print(str(None));

