icecream = "vanilla" # global variable

def foods():
    vegetable = "potato" #local variable
    fruit = "litchi" #local variable
    print(vegetable + " is a local variable value")
    print(fruit + " is a local variable value")
    print(icecream + " is a global variable value")


foods()
# print(vegetable, fruit, icecream) Local variable vegetable and fruit cannot be accessed as it is local to function foods()
print(icecream)