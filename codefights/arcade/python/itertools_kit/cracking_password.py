from itertools import product


def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [int(''.join(words)) for words in product(createNumber([x for x in digits]), repeat=2) if int(''.join(words)) % d == 0]


print(crackingPassword(digits=[1, 5, 2], k=2, d=3))
