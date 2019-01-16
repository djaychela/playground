def multiDivisorSequence_1(nums):
    print(nums)
    divisor = []
    multiple = []
    for i in range(1, len(nums)):
        print(f'divisor - {nums[i - 1]} / {nums[i]} = {nums[i - 1] / nums[i]}')
        divisor.append(nums[i - 1] % nums[i])
        if i >= 2:
            print(f'multiple - {nums[i]} / {nums[i - 2]} = {nums[i] / nums[i - 2]}')
            multiple.append(nums[i] % nums[i - 2])
        else:
            multiple.append(0)

    print(divisor, multiple)

    for i in range(len(divisor)):
        if divisor[i] != 0 and multiple[i] != 0:
            return nums[i + 1]

    return -1


def multiDivisorSequence(nums):
    if nums[0] % nums[1] != 0 and nums[2] % nums[0] != 0:
        return nums[1]
    for i in range(2, len(nums)):
        if (nums[i - 1] % nums[i] != 0) and (nums[i] % nums[i - 2] != 0):
            return nums[i]
    return -1


# nums= [3, 1, 6, 2, 42, 21, 7]
nums = [60, 12, 4, 24, 6, 3, 1, 7]
# nums = [529, 35, 7]
# nums = [10, 5, 20, 4]

print(multiDivisorSequence(nums))
