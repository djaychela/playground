import string

def isBeautifulString(input_string):
    input_list=sorted(list(input_string))
    counts = [input_list.count(chr(i)) for i in range(97,123)]
    for i in range(1,26):
        if counts[i] > counts[i-1]:
            return False
    return True

# from codefights highest submission - simple and beautiful.

def isBeautifulString_2(inputString):
    r = [inputString.count(i) for i in string.ascii_lowercase]
    return r[::-1] == sorted(r)

print(isBeautifulString("bbbaacdafe"))
print(isBeautifulString("aabbb"))
print(isBeautifulString("bbc"))


