def noteFrequency(note):
    lookup = {'A': 0, 'A#': 1, 'Bb': 1, 'B': 2, 'C': -9, 'C#': -8, 'Db': -8, 'D': -7, 'D#': -6, 'Eb': -6, 'E': -5,
              'F': -4, 'F#': -3, 'Gb': -3, 'G': -2, 'G#': -1, 'Ab': -1}
    octave = int(note[-1])
    note = note[:-1]
    pitch = (55 * 2 ** (octave - 1)) * 2 ** (lookup[note]/12)
    return pitch


print(noteFrequency('C5'))
