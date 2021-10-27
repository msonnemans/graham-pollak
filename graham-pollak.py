import math

def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return 1 + f(math.floor(n/2)) + f(math.ceil(n/2))


for i in range(1, 1000):
    if f(i) != i - 1:
        print(f(i))
        print(i - 1)
        break

