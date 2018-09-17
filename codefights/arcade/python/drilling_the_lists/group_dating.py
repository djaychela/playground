def groupDating(male, female):
    return [male[i] for i in range(len(male)) if male[i] != female[i]], [female[i] for i in range(len(male)) if male[i] != female[i]]

def groupDating_1(male, female):
    return list(zip(*[x for x in list(zip(male, female)) if x[0] != x[1]]))


print(groupDating(male=[5, 28, 14, 99, 17], female=[5, 14, 28, 99, 16]))
print(groupDating_1(male=[5, 28, 14, 99, 17], female=[5, 14, 28, 99, 16]))