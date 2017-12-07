def equalise_the_array(array):
    counts = {}
    for a in array:
        count = array.count(a)
        counts[a] = count
    return len(array) - max(counts.values())


print(equalise_the_array([3, 3, 2, 1, 3]))
print(equalise_the_array([4, 6, 5, 3, 1, 2, 3, 4, 7, 8, 6, 4]))
