import timeit


def repeatedDNASequences(s):
    values = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    seq = set()
    rep = set()
    h = 0

    for i in range(len(s)):
        h = 4 * h + values[s[i]]
        if i >= 9:
            # check if found before
            if h in seq:
                rep.add(h)
            seq.add(h)
            # ready for next hash (remove leftmost)
            h -= values[s[i - 9]] * (4 ** 9)

    def decrypt(h2):
        word = ''
        for i in range(10):
            val = h2 % 4
            h2 = h2 // 4
            word = 'ACGT'[val] + word
        return word

    output = [decrypt(h) for h in list(rep)]
    return sorted(output)


def repeatedDNASequences_hash(s):
    h = 0
    values = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    def get_hash(start):
        h = 0
        for i in range(10):
            value = values[s[i + start]]
            h = 4 * h + value
        return h

    seq = set()
    rep = set()
    for i in range(len(s) - 10):
        h1 = get_hash(i)
        if h1 in seq:
            rep.add(h1)
        seq.add(h1)

    def decrypt(h2):
        word = ''
        for i in range(10):
            val = h2 % 4
            h2 = h2 // 4
            word += 'ACGT'[val]
        return word

    output = [decrypt(h) for h in list(rep)]
    return output


def repeatedDNASequences_brute(s):
    repeat_dict = {}
    for i in range(len(s) - 9):
        key = s[i:i + 10]
        if repeat_dict.get(key):
            repeat_dict[key] += 1
        else:
            repeat_dict[key] = 1
    output_list = [k for k, v in repeat_dict.items() if v >= 2]
    output_list.sort()
    return output_list


# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# print(repeatedDNASequences(s))
# # s = "ACCCTCCCACTTGGATGCCGCACGTGTCGACTAACCTTACATTGTCCCCCCACCTCCAGACGGTTAACTCTTGAAATGGGGGAATAGCTGCTTGCGCGTG"
# # print(repeatedDNASequences(s))
# s= "CGACGCAATTTAGAACGGGCCGCACTGCAACCATTGCTCAGACAACGCATGAGTTAAATTTCACAAGTGATAGTGGCTTGCGAGACGTGGGTTGGTGGTAGCGTACGCCCGCTATTCGCCCCTAACGTGACGGGATTATAAGGTCGCTTCCCGGAATGCGCAGACGAGTCTCCGGTTTAGCCTAGACGTCTCACGCGCGCAAGGCGTCAGTTCTCACTATCTCGCACAGGTGTATTCTATTAGTTATGGGTTCTCACTACAGTCGGTTACTTCCTCATCCATTTCTGCATACGGGTCAACTAACAGTGTCATGGGGTATTGGGAAGGATGCGTTTTTAAACCCTCTCAGTAGCGCGAGGATGCCCACAAATACGACGGCGGCCACGGATCTAATGCGAAGCTAGCGACGCTTTCCAGCAACGAGCGCCCCACTTATGACTGCGTGGGGCGCTCCGCTTTCCTAGAGAACATAGATGGTGTTTTCGAATCGTAACCACTTA"
# print(repeatedDNASequences(s))
s = "CCGGCCGGCCGGCCGG"
t = timeit.Timer(lambda: repeatedDNASequences(s))
print(f'rolling hash version: {t.timeit(number=100000)}')
t = timeit.Timer(lambda: repeatedDNASequences_hash(s))
print(f'hash version: {t.timeit(number=100000)}')
t = timeit.Timer(lambda: repeatedDNASequences_brute(s))
print(f'original version:{t.timeit(number=100000)}')
