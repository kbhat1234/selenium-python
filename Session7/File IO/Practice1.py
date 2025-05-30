with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I/o\nusing Java\nI like programming in Java")

with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Javascript")
    print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


def check_for_word(word):
    with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")


def check_for_line(word):
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
    return -1


with open("practice1.txt", "r") as f:
    data = f.read()
    print(data)

check_for_word("learning")
check_for_line("programming")
