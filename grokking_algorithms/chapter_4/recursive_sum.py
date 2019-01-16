def recursive_sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + recursive_sum(array[1:])





data = [1,2,3,4]

print(recursive_sum(data))