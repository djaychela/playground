def greedy_decoding(message):
    decoded = []
    i = 0
    while i < len(message):
        one_digit = int(message[i])
        i += 1
        if i < len(message):
            two_digit = one_digit * 10 + int(message[i])
            if two_digit <= 26:
                decoded.append(chr(two_digit + 64))
                i += 1
                continue
        decoded.append(chr(one_digit + 64))

    return ''.join(decoded)


def greedy_decoding_2(m):
    a = ''

    while m:
        i = [1, 2][m[:2] < '27']
        a += chr(64 + int(m[:i]))
        m = m[i:]

    return a


message = '195318520'

print(greedy_decoding(message))
print(greedy_decoding_2(message))

j = [1,2][False]
print(j)



