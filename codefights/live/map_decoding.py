limit = 1e9 + 7

def mapDecoding(message, i=0, memo={}):
    if i == len(message):
        return 1
    print(i, memo)
    if i in memo.keys():
        return memo[i]
    result = 0
    one_digit = int(message[i])

    if one_digit > 0:
        result += mapDecoding(message, i + 1, memo)

        if i < len(message) - 1:
            two_digit = one_digit * 10 + int(message[i + 1])

            if two_digit <= 26:
                result = int(result + mapDecoding(message, i + 2, memo) % limit)
    memo[i] = result
    return int(result % limit)


# "123" = 3
# "12" = 2
# "11115112112" = 104
# "1221112111122221211221221212212212111221222212122221222112122212121212221212122221211112212212211211" = 782204094
# print(mapDecoding('123'))
# print(mapDecoding("11115112112"))
print(
    mapDecoding("1221112111122221211221221212212212111221222212122221222112122212121212221212122221211112212212211211"))
