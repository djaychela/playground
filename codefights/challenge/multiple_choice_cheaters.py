def multipleChoiceCheaters(a, b, k):
    c = [1 if a[i] == b[i] != k[i] else 0 for i in range(len(k))]
    i = 0
    s = 0
    while i < len(c) - 6:
        if sum(c[i:i+7]) >=4:
            s += 1
            i +=6
        i +=1
    if s*7 > (len(c)/2):
        return True
    return False





studentA =  "BDBABADAAABABAAADBBCCAAACADAAAABAAA"
studentB =  "BCBDDBDDACBBCAAACDCADACDACCBCBBBAAA"
answerKey = "CCBDDDBBBDCDDDCDAABCABBDAACDDDDDCCC"

print(multipleChoiceCheaters(studentA, studentB, answerKey))

#
# studentA = "BACADBBCCACABDA"
# studentB = "BACDDCCCCBCDDBA"
# answerKey = "BACCCACDCCCACDA"
#
# print(multipleChoiceCheaters(studentA, studentB, answerKey))
#
# studentA  = "ABCDAABCBACAB"
# studentB  = "ABCDAABCBACAB"
# answerKey = "ABCDAABCCDBDA"
# print(multipleChoiceCheaters(studentA, studentB, answerKey))
#
#
# studentA  = "AAABBBBBBBBAAA"
# studentB  = "AAABBBBBBBBAAA"
# answerKey = "AAAAAAAAAAAAAA"
# print(multipleChoiceCheaters(studentA, studentB, answerKey))
