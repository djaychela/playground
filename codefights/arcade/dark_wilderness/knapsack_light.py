def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 > maxW and weight2 > maxW:
        return 0
    if weight1 > maxW:
        return value2
    if weight2 > maxW:
        return value1
    if weight1 + weight2 <= maxW:
        return value1 + value2
    return max(value1, value2)