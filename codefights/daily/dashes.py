def dashes(n):
    def sc(i):
        s = '|'
        l = "-" * i
        op.append(s.join(l).center(w, ' '))

    op = []
    w = n * 2 - 1
    for i in range(1, n + 1):
        sc(i)
    for i in range(n - 1, 0, -1):
        sc(i)
    return op


dashes(1)
dashes(2)
dashes(3)
