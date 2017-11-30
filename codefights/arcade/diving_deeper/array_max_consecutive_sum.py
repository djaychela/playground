def arrayMaxConsecutiveSum(inputArray, k):
    highest = 0
    for i in range(len(inputArray)-k+1):
        current = sum(inputArray[i:i+k])
        print(i, current)
        if current > highest:
            highest = current
    return highest


print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))