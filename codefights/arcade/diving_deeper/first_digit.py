def firstDigit(inputString):
    for char in inputString:
        if char.isdigit():
            return char
    return False




firstDigit('aaa123')