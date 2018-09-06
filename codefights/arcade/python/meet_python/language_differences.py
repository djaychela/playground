def division(x,y):
    return x // y


def div_java(x,y):
    return x / y


nums = [(17,13),(-8,2),(-10,3),(5,10),(15,-4)]

for x,y in nums:
    print(division(x,y), div_java(x,y))
