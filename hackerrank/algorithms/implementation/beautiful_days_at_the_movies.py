def beautiful_days_at_the_movies(start, end, divisible):
    counter = 0
    for i in range(start, end+1):
        if (i - beautiful_number(i)) / divisible % 1 == 0:
            counter += 1
    return counter


def beautiful_number(number):
    return int(str(number)[::-1])


def beautiful_days_at_the_movies_2(start, end, divisible):
    counter = sum([1 if ((i-beautiful_number(i)) / divisible % 1 == 0) else 0 for i in range(start, end+1)])
    return counter


print(beautiful_days_at_the_movies(20, 23, 6))
print(beautiful_days_at_the_movies_2(20, 23, 6))

#
# a, b, k = map(int, raw_input().split())
# ans = 0
# for i in range(a, b+1):
#     ans = ans + abs(not (i - int(str(i)[::-1]))%k)
# print ans