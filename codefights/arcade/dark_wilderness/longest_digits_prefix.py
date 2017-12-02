def longestDigitsPrefix(inputString):
    output = ''
    for char in input_String:
        if char.isdigit():
            output += char
        else:
            return output
    return output