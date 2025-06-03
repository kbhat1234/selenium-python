name = "Samuel"
print("Hello, " +name)

print("He said, \"I want to eat an apple.\"")
print('He said, "I want to eat an apple"')
print("He say's i am the greatest assest to any organization.")
print('He say\'s, i am the greatest assest to any organization.')

str1 = """Welcome to python programming.
This is very easy to understand and learn."""
str2 = '''Welcome to python programming.
This is very easy to understand and learn.'''

print(str1, type(str1), id(str1))
print(str2, type(str2), id(str2))

# python strings
fruit = "Mangoes"
len1 = len(fruit)
print(f'{fruit} is {len1} characters long')

str1 ="Welcome "
len1 = len(str1)
print(len1)
print(str1[3:])

alphabets = "ABCDEFG"
for i in alphabets:
    print(i)