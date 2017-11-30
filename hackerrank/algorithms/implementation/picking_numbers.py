def picking_numbers(array):
    array = sorted(array)
    best = 0
    for i in range(len(array)):
        current = array[i]
        running = True
        index = 0
        score = 0
        while running:
            if (i + index) > len(array) - 1:
                running = False
            elif 0 <= array[i + index] - current <= 1:
                score += 1
            elif array[i + index] - current > 2:
                running = False
            index += 1
        if score > best:
            best = score
    return best


print(picking_numbers([4, 6, 5, 3, 3, 1]))

#
# from collections import Counter
# n, arr = input(), Counter(map(int, raw_input().split()))
# print reduce(lambda y, x:max(arr[x] + arr[x + 1], y), range(100), -1)