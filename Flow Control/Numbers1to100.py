# print numbers from 1 to 100
i = 1
while i <= 100:
    print(i, " ")
    i += 1
print(f"End of loop {i}")

# print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
print(f"End of loop {i}")

# print the multiplicatiom table of a number n
i = 1
n = int(input("Enter the number: "))
while i <= 10:
    print(n*i)
    i += 1
print("End of loop")

nums = [10, 20, 30, 40, 50, 60]
index = 0
while index < len(nums):
    print(nums[index])
    index += 1

nums = (10, 20, 30, 40, 50, 60, 40)
n = 40
index = 0
while index < len(nums):
    if(nums[index] == n):
        print(f"{n} Found at index ", index)
        break
    else:
        print("Finding ..")
    index += 1
print("End of loop")

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1


list = [10, 20, 30, 40, 50]
for val in list:
    print(val)
else:
    print("End of Loop")
