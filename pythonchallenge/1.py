text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
text ='map'
lookup = {chr(97+i): chr(97+i+2) for i in range(26)}

answer = ''
for char in text:
    if char in lookup.keys():
        answer += lookup[char]
    else:
        answer += ' '

print(answer)