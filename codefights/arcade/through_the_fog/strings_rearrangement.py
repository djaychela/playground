def stringsRearrangement(inputArray):
    current_test = inputArray
    possibilities = {key: 0 for key in current_test}
    for i in range(len(current_test)):
        for j in range(len(current_test)):
            if i != j:
                this_link = one_letter_different(current_test[i], current_test[j])
                if this_link:
                    possibilities[current_test[i]] += 1
    print(possibilities)
    if 0 in possibilities.values():
        return False
    endpoints = 0
    for p in possibilities.values():
        if p == 1:
            endpoints +=1
    if endpoints !=2:
        return False
    return True


def one_letter_different(str_a, str_b):
    diff = 0
    if len(str_a) != len(str_b):
        return False
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            diff += 1
        if diff > 1:
            return False
    if diff == 1:
        print(str_a, str_b)
        return True
    return False


if __name__ == "__main__":
    stringsRearrangement(["abc", "abx", "axx", "abx", "abc"])
    stringsRearrangement(["f",  "g",  "a",  "h"])

