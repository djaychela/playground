for i in range(26):
    print(f"{chr(97+i)} : {i}")

lookup = {i: chr(97+i) for i in range(26)}
print(lookup)
text = '1917'

for letter in text:
    print(f"{letter}:{lookup[int(letter)]}")

