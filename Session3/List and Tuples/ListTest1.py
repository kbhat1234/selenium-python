list = [99, 100, 77, 89, 99]

print(list); print(type(list))
print(list[4]) # 99
# print(list[5])  # IndexError: list index out of range

print(list[1]) # 100
print(list[2:4]) # [77, 89]
print(list[2:]) # [77, 89, 99]
print(list[:]) # [99, 100, 77, 89, 99]
print(list[:2]) # [99, 100]

print(list[-1]) # 99
print(list[-2:4]) # [89]
print(list[-4:-2]) # [100, 77]