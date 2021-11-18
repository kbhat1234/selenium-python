for i in range(1, 10):
    if i == 7:
        print("breaking the loop")
        break
    print(i)

cart = [10, 20, 600, 60, 70, 560, 90]
cart.sort();
print(type(cart.sort()))
# print(type(s))
# print(s)
for item in cart:
    if item > 500:
        print("{} cannot process this order, it requires insurance ".format(item))
        continue
    print("processing item: ", item)

for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)

numbers = [10, 20, 0, 5, 0, 30]
for n in numbers:
    if n == 0:
        print("pagal hogaya")
        continue
    print("100/{}={}".format(n, 100 / n))

cart = [10, 20, 500, 556, 33, 99]
for item in cart:
    if item > 500:
        print("Sorry we cannot process your request...", item, " insurance is required")
        continue
    print("Processing item: ", item)
else:
    print("Congrats...all items processed successfully")
