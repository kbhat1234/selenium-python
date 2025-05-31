icecream = "vanilla"

def foods():
    vegetable = "potato"
    fruit = "banana"
    global icecream
    print(vegetable + " is a local variable value")
    print(fruit + " is a local variable value")
    print(icecream + " is a local variable value")


foods()
print(icecream)

