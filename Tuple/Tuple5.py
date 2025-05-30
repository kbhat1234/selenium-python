t = eval(input("Enter any tuple numbers:"))
sum = 0
l = len(t)
for x in t:
    sum = sum + x
print("Sum is ", sum)
print("Average is ", sum/l)