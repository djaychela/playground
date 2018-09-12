from collections import deque


def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    print(res)
    deque(map(lambda i: res[i].rotate(-i), range(n)), 0)
    return [list(d) for d in res]


digits = [1, 2, 3, 4, 5]
print(doodledPassword(digits))
