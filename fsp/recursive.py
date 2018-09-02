def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def integer_sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + integer_sum(x-1)


def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


print(fibonacci(8))
