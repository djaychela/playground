import string

def isBeautifulString(input_string):
    input_list=list(input_string)
    input_list=sorted(input_list)
    counts = []
    for i in range(97,123):
        counts.append(input_list.count(chr(i)))
    for i in range(1,26):
        if counts[i]>counts[i-1]:
            return False
    return True

# from codefights highest submission - simple and beautiful.

def isBeautifulString_2(inputString):
    r = [inputString.count(i) for i in string.ascii_lowercase]
    return r[::-1] == sorted(r)

print(isBeautifulString_2("bbbaacdafe"))
print(isBeautifulString_2("aabbb"))
print(isBeautifulString_2("bbc"))


