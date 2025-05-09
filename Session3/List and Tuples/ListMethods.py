list = [12, 9, 5, 22, 3, 6, 7, 3]
list.append(6) # will append 6 to end of the list
print(list) # [12, 9, 5, 22, 3, 6]

list.reverse()
print(list)

list.sort() # sort the list in ascending order by default
print(list) # [3, 5, 6, 9, 12, 22]

list.sort(reverse=True) # sort the list in decending order.
print(list) # [22, 12, 9, 6, 5, 3]

list.reverse() # reverses the list
print(list) # [3, 5, 6, 9, 12, 22]

list.insert(1, 11) # insert element 11 at index 1
print(list) # [3, 11, 5, 6, 9, 12, 22]

list.remove(3) # removes first occurence of the 3 from the list
print(list) # [11, 3, 5, 6, 6, 7, 9, 12, 22]

list.pop(3) # removes element at index 3
print(list) # [11, 3, 5, 6, 7, 9, 12, 22]

list2 = list.copy()
print(list2)