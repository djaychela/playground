def isLucky(n):
    n_str = str(n)
    n_len = int(len(n_str) / 2)
    first = n_str[:(n_len)]
    second = n_str[n_len:]
    f_sum = sum([int(f) for f in first])
    s_sum = sum([int(s) for s in second])
    return f_sum == s_sum



print(isLucky(1230))