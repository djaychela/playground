def studyOrSleep_1(familiarity, hoursRemaining):
    done = False
    best = familiarity
    penalty = 0
    study_hours = 0
    while not done:
        unfamiliarity = (100 - familiarity) * 0.8
        familiarity = (100 - unfamiliarity)
        score = familiarity
        if hoursRemaining <= 8:
            penalty += 5
            score -= penalty
        print(f'fam: {familiarity}, sc:{score}, ')
        if score < best:
            done = True
        else:
            best = score
            hoursRemaining -=1
            study_hours += 1
        if hoursRemaining == 0:
            done = True

    return study_hours

# do this as a list comprehension and then return index(max(list))

def studyOrSleep(familiarity, hoursRemaining):
    if hoursRemaining == 0:
        return 0
    if hoursRemaining == 1:
        return 1
    score = []
    penalty = 0
    for i in range(hoursRemaining):
        if hoursRemaining < 8:
             penalty += 5
        score.append(familiarity - penalty)
        familiarity = (100 - (100-familiarity) * 0.8)
        hoursRemaining -=1
    print(score)
    return score.index(max(score))


# familiarity = 64
# hoursRemaining = 8
# # output should be 2

# familiarity = 38
# hoursRemaining = 9
# # output should be 5

familiarity = 75
hoursRemaining = 8

# familiarity = 75
# hoursRemaining = 8
# # output should be 0

print(studyOrSleep(familiarity, hoursRemaining))