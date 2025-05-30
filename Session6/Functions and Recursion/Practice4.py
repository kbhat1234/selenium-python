def calsum(n):
    if (n == 0):
        return 0
    else:
        return calsum(n-1) + n


s = calsum(4)
print(s)