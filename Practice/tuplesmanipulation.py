countries = ("Spain", "Italy", "India", "China", "Germany", "Romania")
temp = list(countries)
print(countries, type(countries), id(countries))  # ('Spain', 'Italy', 'India', 'China', 'Germany', 'Romania') <class 'tuple'> 2254182787072
print(temp, type(temp), id(temp))  # ['Spain', 'Italy', 'India', 'China', 'Germany', 'Romania'] <class 'list'> 2254183471680
temp.append("Russia")
print(temp)  # ['Spain', 'Italy', 'India', 'China', 'Germany', 'Romania', 'Russia']
temp.insert(3, "Bangladesh")
print(temp)  # ['Spain', 'Italy', 'India', 'Bangladesh', 'China', 'Germany', 'Romania', 'Russia']
temp.pop(4)
print(temp)  # ['Spain', 'Italy', 'India', 'Bangladesh', 'Germany', 'Romania', 'Russia']
temp[2] = "Finland"
print(temp)  # ['Spain', 'Italy', 'Finland', 'Bangladesh', 'Germany', 'Romania', 'Russia']
countries = tuple(temp)
print(countries)  # ('Spain', 'Italy', 'Finland', 'Bangladesh', 'Germany', 'Romania', 'Russia')

# Concatenate 2 tuples using + operator
tuple1 = (1, 3, 4, 5, 2, 9,7)
tuple2 = ("red", "yellow", "green", "blue")
concat = tuple1 + tuple2
print(concat)
