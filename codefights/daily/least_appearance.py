import operator


def leastAppearance(choices):
    array = []
    for choice in choices:
        options = {}
        for entry in sorted(choice):
            options[entry] = array.count(entry)
        options_s = sorted(options.items(), key=operator.itemgetter(1))
        print(options, options_s)
        array.append(options_s[0][0])
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