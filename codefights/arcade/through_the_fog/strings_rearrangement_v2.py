import itertools

def stringsRearrangement(inputArray):
    list_of_elements = list(range(len(inputArray)))
    possibilities = itertools.permutations(list_of_elements,len(inputArray))
    for p in possibilities:
        this_attempt = True
        for j in range(len(p)-1):
            if not one_letter_different(inputArray[p[j]], inputArray[p[j+1]]):
                this_attempt = False
        if this_attempt:
            print(f"success - {p}")
            for j in range(len(p)):
                print(inputArray[p[j]])
            return True
    return False

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
        return True
    return False


if __name__ == "__main__":
    stringsRearrangement(["abc", "abx", "axx", "abx", "abc"])
    stringsRearrangement(["f",  "g",  "a",  "h"])

