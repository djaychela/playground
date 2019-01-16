def theJanitor(word):
    left = [0] * 26
    right = [0] * 26
    was = [0] * 26
    for i in range(26):
        left.append(0)
        right.append(0)
        was.append(False)

    for i in range(len(word)):
        c = ord(word[i]) - ord('a')
        if not was[c]:
            left[c], was[c] = i, True
        right[c] = i

    print(left)
    print(right)
    print(was)

    ans = []
    for i in range(26):
        ans.append(right[i] - left[i] + 1 if was[i] else 0)
    return ans


# Input:
#
# word: "likemm"
#
# Output:
#
# [0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 3, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# Expected Output:
#
# [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# Console Output:
#
# Empty


word = "abacaba"
#
# Output:
#
# [7, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# Expected Output:
#
# [7, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# Console Output:
#
# Empty

print(theJanitor(word))
