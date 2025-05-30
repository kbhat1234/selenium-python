with open("demo.txt", "r") as f:
    data = f.read()
    print(f'File data is {data}')
    print(id(data))

with open("demo1.txt", "r+") as f:
    data = f.read()
    print(data)
    f.write("This is new text")

