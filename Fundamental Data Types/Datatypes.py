a = 10;
print(f'value of a is {a}');
print(type(a));
b = 10.5;
print(b);
print(type(b));
true = True;
false = False;
print(f'true is {true}, and false is {false}');
print(f'{type(true)} and  {type(false)}');
print(id(a));

num = 3432434234234234234324;
print(type(num));

#  decimal form (base-10) (0 to 9)
a = 202;
print(a);

# binary form (base-2) (0 and 1) 0b | 0B
a = 0b10001;
print(a);

# gives syntax error: invalid digit '3' in binary literal
# a = 0b1013;
# print(a);

# octal form (base-8) (0 to 7) 0o | 0O
a = 0o3442;
print(a);

# gives syntax error: invalid digit '9' in octal literal
# a = 0o3449;
# print(a);

# hexadecimal form (base-16) (0 to 9) and (A to F or a to f) 0x | 0X
a = 0x11;
print(a);

a = 0x1233;
print(a);

a = 0x22BF;
print(a);

# gives syntax error: invalid hexadecimal literal
# a = 0x9ACDFS;
# print(a);


# Base conversions functions
print(bin(10));
print(bin(0xFace));
print(bin(0o74));

print(oct(10));
print(oct(0b1001011));
print(oct(0x15));

print(hex(15));
print(hex(0b1011));
print(hex(0o37));
