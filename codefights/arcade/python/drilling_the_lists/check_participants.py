import itertools


def checkParticipants(participants):
    return [idx for idx, p in enumerate(participants) if idx > p]


def checkParticipants_2(participants):
    return [i for i, p in enumerate(participants) if i > p]


print(checkParticipants([0, 1, 1, 5, 4, 8]))
print(checkParticipants_2([0, 1, 1, 5, 4, 8]))
