def recursive_count(array):
    if len(array) == 0:
        return 0
    else:
        return 1 + recursive_count(array[1:])


print(recursive_count([1, 2, 3, 4, 5, 6, 7]))
