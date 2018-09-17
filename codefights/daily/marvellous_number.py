def marvelousNumber(n):
    output = ''
    for c in n:
        if c == '4' or c == '7':
            output += c
        elif c in ['5', '6']:
            output += '7'
        else:
            output += '4'
    return output


print(marvelousNumber(n="1511"))
