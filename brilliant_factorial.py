import math

def brilliant(x):
    numerator = math.factorial(x+2) * math.factorial(x)
    denominator = math.factorial(x+1) + math.factorial(x)
    answer = math.factorial(x+1)
    return (numerator/denominator == answer)

print(brilliant(3))
