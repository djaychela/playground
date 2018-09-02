import math
from decimal import Decimal


def latticevillePaths(m, n):
    def nCr(n, r):
        f = math.factorial
        term1 = Decimal(f(n))
        term2 = Decimal(f(r))
        term3 = Decimal(f(n-r))
        print(f"nCr: {term1}, {term2}, {term3}")
        return Decimal(term1 / term2 / term3)

    def narayana(m, n):
        term1 = Decimal(1 / m)
        term2 = round(Decimal(nCr(m, n)))
        term3 = round(Decimal(nCr(m, n - 1)))
        print(f"nar:  m{m}, {term1}, {term2}, {term3}")
        return Decimal(term1 * term2 * term3)

    if m <= 2 or n <= 2:
        return 1
    if m < n:
        m, n = n, m
    answer = narayana(m + (-3 + n), n - 1)
    mod = 7 + 10 ** 9
    answer = round(answer)
    return answer,  answer % mod


# for i in range(1,8):
#     for j in range(1,8):
#         print(f'For {i}*{j} : {latticevillePaths(i, j)}')

i=1000
j=1003
print(f'For {i}*{j} : {latticevillePaths(i, j)}')