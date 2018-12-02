def celsiusVsFahrenheit_1(yourTemps, friendsTemps):
    score = 0
    for i in range(len(friendsTemps)):
        if yourTemps[i] * 9 / 5 + 32 < friendsTemps[i]:
            score += 1
    return score


def celsiusVsFahrenheit(yourTemps, friendsTemps):
    score = sum(1 for x, y in zip(yourTemps, friendsTemps) if x * 9 / 5 + 32 < y)
    return score



yourTemps = [25, 32, 31, 27, 30, 23, 27]
friendsTemps = [78, 83, 86, 88, 86, 89, 79]
print(celsiusVsFahrenheit(yourTemps, friendsTemps))