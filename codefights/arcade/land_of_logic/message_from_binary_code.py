def messageFromBinaryCode(code):
    characters = [code[i:i + 8] for i in range(0, len(code), 8)]
    output = ''
    for char in characters:
        output += chr(int(str(char), 2))
    return output





print(messageFromBinaryCode("010010000110010101101100011011000110111100100001"))