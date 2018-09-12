from random import randint
import datetime


def countSmallerToTheRight(nums):
    counts = {len(nums)-1:0}
    for i in range(len(nums)-1, -1,-1):
        counts[i]=0
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                # print(i, j, nums[i], nums[j], counts)
                counts[i] += 1
            elif nums[i] == nums[j]:
                counts[i] += counts[j]
                # print(i, j, nums[i], nums[j], counts)
                break

    return sum(counts.values())


# print(countSmallerToTheRight([3, 8, 4, 1]))
# print(countSmallerToTheRight([1, 0, 2]))
# print(countSmallerToTheRight([5, 3, 2, 4, 4, 35, 1, 14, 38, 35, 2]))


test_len = 10000
test_list = [randint(-10000, 10000) for i in range(test_len)]
print('starting')
start_time = datetime.datetime.now()
print(countSmallerToTheRight(test_list))
end_time = datetime.datetime.now()
print('finished')
print(end_time - start_time)