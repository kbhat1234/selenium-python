# Ascending order - sort() default reverse=False
list1 = [10, 4, 2,7, 5, 9, 3]
print(list1)
list1.sort() # ascending order
print(list1)

# Desending order - sort(reverse=True)
list2 = [0, 7, 3, 2, 1, 8, 4]
print(list2)
list2.sort(reverse=True) # desending order
print(list2)

# reversing the given list - reverse()
colors = ["Red", "Green", "Pink", "Yellow"]
colors.reverse()
print(colors) # ['Yellow', 'Pink', 'Green', 'Red']

num = [9, 2, 4, 5, 3, 4, 2]
num.reverse()
print(num) # [2, 4, 3, 5, 4, 2, 9]

# index() method - returns the index of first occurence of the list item
colors = ["Blue", "Red", "Pink", "Green", "Yellow", "Green"]
print(colors.index("Green"))
# print(colors.index("Pinky")) # ValueError: 'Pinky' is not in list

# count() method - returns the count of no. of items with given value
colors = ["Blue", "Red", "Pink", "Green", "Yellow", "Green", "Yellow"]
print(colors.count("Yellow"))

# copy() method - returns a copy of the list
colors = ["Blue", "Red", "Pink", "Green", "Yellow", "Green", "Yellow"]
newlist = colors.copy()
print(newlist) # ['Blue', 'Red', 'Pink', 'Green', 'Yellow', 'Green', 'Yellow']
