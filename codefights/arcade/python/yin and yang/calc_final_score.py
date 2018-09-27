def calcFinalScore(scores, n):
    gen = (s**2 for s in sorted(scores, reverse=True))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res


print(calcFinalScore([4, 2, 4, 5], 3))