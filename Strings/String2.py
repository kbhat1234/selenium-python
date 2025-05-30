# Membership operator
s = "durga software"
print('durga' in s)
print('Durga' not in s)
print('Durga' in s)
print('durga' not in s)

# substring in string
str1 = input("Enter any string: ")
substr1 = input("Enter the substring: ")
if substr1 in str1:
    print("substring '{}' part of string '{}'".format(substr1, str1))
else:
    print("substring '{}' not part of string'{}'".format(substr1, str1))

str1 = "Welcome to India"
str2 = "welcome to india"

print(str1 > str2)
print(str1 >= str2)
print(str1 < str2)
print(str1 <= str2)
print(str1 == str2)

str3 = input("enter first string: ")
str4 = input("enter second string: ")
if str3 == str4:
    print("both strings are equal")
# elif str3 != str4:
# print("both strings are not equal")
elif str3 < str4:
    print("{} is smaller than {}".format(str3, str4))
else:
    print("'{}' is greater than '{}'".format(str3, str4))

l1 = ["A", "B", "C"]
l2 = ["A", "B", "C"]
print(l1, l2)
print(l1 is l2)
print(id(l1), id(l2))
l3 = l2
print(l3)
print(id(l3))
print(l1 is l2)  # False
print(l2 is l3)  # True


# Remove spaces in the input using strip(), lstrip() and rstrip()
city = input("Enter your city name: ")
print(city.rstrip())
li = ["Bangalore", "Hyderabad", "Kolkata", "Delhi", "Mumbai"]
if city.rstrip() in li:
    print("Your '{}' city is available and CCC no. is 9887377373".format(city.rstrip()))
else:
    print("Please enter valid city name to proceed")