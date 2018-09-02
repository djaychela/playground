import datetime

start = datetime.datetime.strptime('24 11 1892','%d %m %Y')
end = datetime.datetime.strptime('01 01 2000','%d %m %Y')

print(end-start)

lookup = {i: chr(97+i) for i in range(26)}

text = '39118'

for letter in text:
    print(f"{letter}:{lookup[int(letter)]}")