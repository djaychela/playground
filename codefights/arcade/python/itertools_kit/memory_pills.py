from itertools import dropwhile, chain, cycle


def memoryPills(pills):
    gen = chain((dropwhile(lambda x: len(x) % 2 != 0, pills)),cycle(['']))
    print(next(gen))
    return [next(gen) for _ in range(3)]


pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]
print(memoryPills(pills))
