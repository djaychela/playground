def getPoints(answers, p):
    questionPoints = lambda i, ans: i if ans else -2

    res = 0
    for i, ans in enumerate(answers):
        print(questionPoints(i, ans))
        res += questionPoints(i, ans)
    return res


print(getPoints([True, True, False, True], 2))