# def mathMarking(s):
#     p = s.split('=')
#     a = [int(eval(q)) for q in p]
#     s = 0
#     for i in range(len(a) - 1):
#         if a[i] == a[i + 1]:
#             s += 1
#     return str(s) + ' / ' + str(len(p) - 1)


def mathMarking(s):
    p = s.split('=')
    a = [int(eval(q)) for q in p]
    s = sum([1 for i in range(len(a) - 1) if a[i] == a[i+1]])
    return str(s) + ' / ' + str(len(p) - 1)


solution = "3 + 2 = 5"
print(mathMarking(solution))

solution = "7 - 3 * 2 + 1 = 4 * 2 + 1 = 8 + 1 = 9"
print(mathMarking(solution))

solution = "-50 + 66 / 11 + 645 = -50 + 6 + 645 = -50 + 661 = -711"
print(mathMarking(solution))
