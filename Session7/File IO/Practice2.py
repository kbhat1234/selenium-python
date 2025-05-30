import os

with open("DEMO.txt", "w") as f:
    f.write("Welcome to python programming")

with open("DEMO.txt", "r") as f:
    data = f.read()
    print(data)

with open("DEMO.txt", "w") as f:
    f.write("Welcome")

# with open("IMG-20250403-WA0039.jpg", "rb") as f:
#   data = f.read()
#  print(data)

# with open("IMG-20250403-WA0039.jpg", "wb") as f:
# f.write("xffxd8")

with open("DEMO.txt", "r+") as f:
    data = f.read()
    print(data)
    f.write(" to python programming")

with open("DEMO.txt", "w+") as f:
    f.write(" Hello world")

with open("DEMO.txt", "a") as f:
    f.write(". This is a new text added")

with open("DEMO.txt", "a+") as f:
    f.write("New lines added")

result = os.path.abspath(__file__)
print(result)
print(type(result))

file_path = "C:\\Users\\admin\\PycharmProjects\\pythonlearning\\Session6\\Session7\\File IO\\DEMO.txt"
filename = os.path.basename(file_path)
print("The file name obtained is:", filename)

current_name = "DEMO.txt"
new_name = "demo.txt"
os.rename(current_name, new_name)
print(f'File {current_name} renamed to {new_name} successfully')
# with open("new.txt", "x") as f:
#   f.write("Welcome to java")


# os.remove("DEMO.txt")
# os.remove("practice.txt")
