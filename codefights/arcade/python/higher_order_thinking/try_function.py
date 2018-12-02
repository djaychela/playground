import math

def tryFunctions(x, functions):
    return [eval(f)(x) for f in functions]


functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"]
x = 1

print(tryFunctions(x, functions))