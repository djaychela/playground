def circular_array_rotation(array, rotation, queries):
    index = rotation % len(array)
    for query in queries:
        print(array[(query - index) % len(array)])


print(circular_array_rotation([1, 2, 3], 2, [0, 1, 2]))
