def electionsWinners(votes, k):
    win = max(votes)
    winners = 0
    for vote in votes:
        if vote + k > win:
            winners += 1
    return max(1, winners)


print(electionsWinners([2, 3, 5, 2], 3))
print(electionsWinners([5, 1, 3, 4, 1],0))