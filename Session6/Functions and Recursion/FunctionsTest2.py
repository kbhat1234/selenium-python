def calc_sum(a, b):
    s = a + b
    return s


def cal_sum(a, b):
    s = a+ b
    print(f'Sum of {a} and {b} is {s}')


def hello_func():
    print("Welcome to python functions", end=" ")
    print("this is is easy and fast", end="\n")
    print("this os next line of words")

def avg_sum(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

def avg_s(a, b, c):
    s = a + b + c
    avg = s / 3
    print(f'Average  of {a} {b} {c} is {avg}')



s1 = calc_sum(10, 5) # passing the arguments to the calling function and the function returns value of sum to the called function.
print(f'sum is {s1}')
cal_sum(10, 6)
cal_sum(10, 66)
hello_func()
hello_func()
hello_func()
avg = avg_sum(10, 20, 30)
print(f'Average is {avg}')
avg_s(20, 20, 20)