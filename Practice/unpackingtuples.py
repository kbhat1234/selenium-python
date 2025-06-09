fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals, birds, fish) = fauna
# (*animals, *birds, *fish) = fauna  # SyntaxError: multiple starred expressions in assignment
print("Animals: ", animals)
print("Birds: ", birds)
print("Fish: ", fish)

(birds, *animals, fish) = fauna
print("Birds: ", birds)
print("Animals: ", animals)
print("Fish: ", fish)

(birds, fish, *animals) = fauna
print("Birds: ", birds)
print("Animals: ", animals)
print("Fish: ", fish)