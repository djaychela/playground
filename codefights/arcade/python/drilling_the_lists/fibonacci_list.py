import functools

def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])]


print(fibonacciList(6))

# Why the hell would anyone do this?  You'd kill anyone you knew who actually wrote this code with a free hand.