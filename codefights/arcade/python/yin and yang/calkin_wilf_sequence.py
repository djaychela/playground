def calkinWilfSequence(number):
    def fractions():
        ...

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res


print(calkinWilfSequence([1,3]))