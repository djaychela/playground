import math


def primesSum(a, b):
    # return [x for x in range(a, b + 1) if x in list(filter(lambda c: all(c % num for num in range(2, c)), range(2, b+1)))]
    # return [x for x in list(filter(lambda c: all(c % num for num in range(2, c)), range(2, b+1))) if x in range(a, b)]
    return sum(filter(lambda x: all(x % i for i in range(2, int(x ** 0.5) + 1)), range(max(2, a), b + 1)))


print(primesSum(10, 20))
print(primesSum(13,13))

# print(filter(lambda p: all(p % n for n in range(3, int(math.sqrt(p)) + 1, 2)), range(3, max, 2)))

prime = 13
print(list(filter(lambda prime: all(prime % num for num in range(2, prime)), range(2, prime+1))))
