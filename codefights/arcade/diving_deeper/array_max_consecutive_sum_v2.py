def arrayMaxConsecutiveSum(inputArray, k):
    current = sum(inputArray[0:k])
    highest = current
    for i in range(1,len(inputArray)-k+1):
        current -= inputArray[i-1]
        current += inputArray[i+k-1]
        if current > highest:
            highest = current
    return highest

print(arrayMaxConsecutiveSum([3, 2, 1, 1],1))
# print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6,4,7,2,4,3,2,1,7,8], 2))