def buildPalindrome(st):
    best = 1
    rev_st = st[::-1]
    for i in range(len(st),0,-1):
        print(st[i-1:], i, len(rev_st), len(rev_st) + 1 - i, rev_st[:(len(rev_st) +1 - i)],best)
        if (st[i-1:]) == (rev_st[:(len(rev_st) +1 - i)]):
            print(st[i-1:]), (rev_st[:(len(rev_st) +1 - i)])
            best = len(st)-i+1
            print(f"best:{best}")
    print(best)
    output = st + rev_st[best:]
    return output


def build_palindrome_codefights(str):
    for i in range(len(str)):
        s = str + str[i::-1]
        print(s)
        if s == s[::-1]:
            return s

def build_palindrome_codefights_3(s):
    for i in range(len(s)):
        p=s[:i+1]+s[:i][::-1]
        print(p)
        if s in p:
            return p



print(build_palindrome_codefights('abcdc'))
print(build_palindrome_codefights('abcdefgfe'))
