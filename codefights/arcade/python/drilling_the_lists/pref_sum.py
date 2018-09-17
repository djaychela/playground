import functools

def prefSum(a):
    return functools.reduce(lambda c, x: c + [c[-1] + x], a, [0])[1:]


print(prefSum(a=[1, 2, 3]))
