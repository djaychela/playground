import math


def latticevillePaths(m, n):
    def nCr(n, r):
        f = math.factorial
        return f(n) // f(r) // f(n - r)
    def narayana(m,n):
        term1 = 1 / m
        term2 = nCr(m, n)
        term3 = nCr(m, n - 1)
        return term1 * term2 * term3
    if m <=2 or n <=2:
        return 1
    if m < n:
        m,n = n,m
    return narayana(m+(-3+n),n-1)


i = 1000
j = 1000

print(f'For {i}*{j} : {latticevillePaths(i, j)}')
