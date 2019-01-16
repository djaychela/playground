def waveformRecognition_2(unknownWave, waveDatabase):
    best_score = 100000
    best_index = -1
    for idx, wave in enumerate(waveDatabase):
        for i in range(0, len(wave) - len(unknownWave)):
            this_diff = 0
            for j in range(len(unknownWave)):
                curr_diff = unknownWave[j] - wave[i + j]
                if curr_diff < 0:
                    curr_diff = 100000
                this_diff += curr_diff
            if this_diff < best_score:
                best_score = this_diff
                best_index = idx

    return best_index


def waveformRecognition(unknownWave, waveDatabase):
    best_score = 100000
    best_index = -1
    for idx, wave in enumerate(waveDatabase):
        for i in range(0, len(wave) - len(unknownWave)):
            this_diff = sum([unknownWave[j] - wave[i + j] if unknownWave[j] - wave[i + j] >= 0 else 100000 for j in
                             range(len(unknownWave))])
            if this_diff < best_score:
                best_score = this_diff
                best_index = idx

    return best_index


# unknownWave = [3, 8, 8, 4, 10, 7]
# waveDatabase = [[8, 4, 4, 1, 2, 1, 1, 4, 3, 3, 3, 1, 4, 2, 1, 2, 10],
#                 [2, 2, 1, 2, 5, 10, 9, 1, 7, 3, 6, 2, 8, 4, 1],
#                 [9, 3, 2, 3, 3, 3, 7, 3, 7, 6, 2, 7, 4, 5, 2, 2],
#                 [2, 8, 2, 4, 2, 6, 3, 8, 3, 8, 8, 1, 1, 1, 5, 7, 1],
#                 [3, 7, 1, 3, 10, 2, 1, 1, 2, 1, 1, 6, 4, 6, 4, 1, 8]]

unknownWave = [2, 4, 2, 6, 8]
waveDatabase = [[0, 2, 7, 6, 0, 5, 6, 9],
                [6, 0, 3, 0, 10, 1, 8, 3, 1, 0]]

print(waveformRecognition(unknownWave, waveDatabase))
