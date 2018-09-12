def competitiveEating(t, width, precision):
    return '{:.{precision}f}'.format(t, precision=precision).center(width)


print(competitiveEating(3.1415,10,2))