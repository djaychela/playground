from collections import Counter
from random import randint


def modeScores_1(scores):
    output = []
    for i in range(1, len(scores) + 1):
        curr_scores = scores[:i]
        curr_count = Counter(curr_scores)
        best = (0, 0)
        for k, v in curr_count.items():
            if v > best[1]:
                best = (k, v)
            elif v == best[1] and k > best[0]:
                best = (k, v)
        # print(best, curr_count, curr_scores)

        output.append(best[0])
    return output


def modeScores(scores):
    output = []
    freqs = {}

    def get_mode(freq):
        mode = -1
        max_freq = 0
        for num in freq.keys():
            if freq[num] > max_freq or (freq[num] == max_freq and num > mode):
                max_freq = freq[num]
                mode = num
        return mode

    for i in range(len(scores)):
        if scores[i] not in freqs.keys():
            freqs[scores[i]] = 0
        freqs[scores[i]] += 1
        output.append(get_mode(freqs))
    return output


scores = [randint(1, 100) for _ in range(50000)]


# scores = [75, 81, 75, 90]
print(modeScores(scores))
