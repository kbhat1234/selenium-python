def sum(a, b):
    s = a +b
    print(f'sum of {a} and {b} is {s}')

def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
sum(a, b)

cal_avg(10, 23, 45)
