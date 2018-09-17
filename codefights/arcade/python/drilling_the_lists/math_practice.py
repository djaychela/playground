import functools


def mathPractice(numbers):
    return functools.reduce(lambda acc, x: (acc + x[1] if x[0] % 2 else acc * x[1]), enumerate(numbers), 1)


print(mathPractice(numbers=[1, 2, 3, 4, 5, 6]))
