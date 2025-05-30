from sys import argv

"""
print(argv[1])
print(type(argv))
for x in argv[1:]:
    print(x)

print(eval(argv[1])+eval(argv[2]))
print(type(argv))
print(argv)
print(argv[1:])
print(argv[1:3:1])
print(argv[:])
print(argv[0], argv[1])


print("The no.of command line arguments: ", len(argv))
print("The list of command line arguments: ", argv)
print("command line arguments one by one")
for x in argv:
    print(x)
print("slice operator result: ", argv[1:5])
"""
# read the values from command line and print the sum
args = argv[1:]
print(type(args))
s = 0
for x in args:
    n = int(x)
    s = s + n
print(s)

print(argv)
