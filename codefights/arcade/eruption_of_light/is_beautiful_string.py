def isBeautifulString(inputString):
    input_list = list(inputString)
    input_list = sorted(input_list)
    input_chr = list(set(input_list))
    input_chr = sorted(input_chr)
    count = input_list.count(input_chr[0])
    print(input_list, input_chr, count)
    del input_chr[0]
    print(input_chr)
    for char in input_chr:
        print(input_list.count(char), count)
        if input_list.count(char) > count:
            return False
        count = input_list.count(char)
    return True


print(isBeautifulString("bbbaacdafe"))
print(isBeautifulString("aabbb"))
print(isBeautifulString("bbc"))
