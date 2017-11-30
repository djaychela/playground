def extractEachKth(inputArray, k):
    limit = (len(inputArray)//k)*k
    print(limit)
    for i in range (limit, 0, -k):
        del inputArray[i-1]
    return inputArray


print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))