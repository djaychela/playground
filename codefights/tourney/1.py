def arrayPreviousLess(items):
    output = []
    for i in range(len(items)):
        done = False
        for j in range(i,-1, -1):
            if items[j] < items [i]:
                output.append(items[j])
                done = True
                break
        if not done:
            output.append(-1)
    return output



items =  [3, 5, 2, 4, 5]

# Output:
#
# [-1, -1, 5, -1, -1, -1, -1, 4, -1, 5]
#
# Expected Output:
#
# [-1, 3, -1, 2, 4]

print(arrayPreviousLess(items))

#
# Input:
#
# items: [7, 7, 8, 3, 4, 4, 2, 5, 6, 7, 7]
#
# Output:
#
# [-1, -1, -1, -1, 8, -1, -1, -1, -1, -1, 4, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, 6, -1, 7, -1, -1, 7]
#
# Expected Output:
#
# [-1, -1, 7, -1, 3, 3, -1, 2, 5, 6, 6]
#
# Console Output:
#
# Empty