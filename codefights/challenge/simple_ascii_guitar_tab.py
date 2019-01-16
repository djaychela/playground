def simpleASCIIGuitarTab(notes):
    lookup = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4,
              'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    output = ['e |', 'B |', 'G |', 'D |', 'A |', 'E |']
    c3 = [20, 15, 10, 5, 1, -4]
    notes = notes.split()

    def add(tab, st, ft, fill='-'):
        for idx, _ in enumerate(tab):
            if idx == st:
                tab[idx] += str(ft)
            else:
                tab[idx] += fill

    add(output, -1, -1, '-')

    for note in notes:
        pitch = note[:-1]
        oc = int(note[-1:])
        f1 = [f + ((oc - 4) * 12) + lookup[pitch] for f in c3]
        frets = [f if f in range(6) else 40 for f in f1]
        string = 5 - frets.index(min(frets))
        fret = min(frets)
        add(output, string, fret)
        add(output, -1, -1, '-')

    add(output, -1, -1, '|')

    return output


notes = "A2"
# expected: ["e |-3-|",
#  "B |---|",
#  "G |---|",
#  "D |---|",
#  "A |---|",
#  "E |---|"]

print(simpleASCIIGuitarTab(notes))


# Winning version:

# s,*g = eval(dir()[0])
# for c in "eBGDAE":
#     c += " |"
#     for n, *a, o in s.split():
#         x = ord(n)*13//8%12 + 12*int(o) + len(a) - 53
#         x += x > -7
#         c += "-%s" % (len(g)+x//5 and '-' or x%5)
#     g += c + "-|",
# return g