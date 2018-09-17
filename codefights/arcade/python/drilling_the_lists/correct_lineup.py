def correctLineup(athletes):
    return [y for x in list(zip(athletes[1::2], athletes[::2])) for y in x]


print(correctLineup(athletes=[1, 2, 3, 4, 5, 6]))

print([y for x in [(2, 1), (4, 3), (6, 5)] for y in x])
