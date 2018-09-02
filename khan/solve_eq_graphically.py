import math


def g(x):
    # return -5 * (0.6** x ) -2
    return 3 * math.log( -x, 3)


for i in range(-10, 0):
    print(f"{i}: {g(i)}")
