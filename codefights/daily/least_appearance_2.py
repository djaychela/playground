import operator


def leastAppearance(choices):
    array = []
    for choice in choices:
        current = []
        for entry in sorted(choice):
            current.append(array.count(entry))

        array.append(sorted(choice)[current.index(min(current))])
    return array


print(leastAppearance([[1, 2], [3, 4], [1, 2]]))
print(leastAppearance([[4,8],
 [92,92],
 [9,53],
 [44,48],
 [2,67],
 [3,3],
 [60,93],
 [18,37],
 [7,15],
 [2,4]]))

# [4, 92, 9, 44, 2, 3, 60, 18, 7, 2]