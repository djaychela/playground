def longestWordLadder(startWord, goalWord, usableWords):
    chain = []
    chain.append([startWord])
    usableWords.append(goalWord)
    usableWords.append(startWord)
    solutions = []
    # print(usableWords)

    def check_distance(sw, gw):
        distance = sum([1 for swl, gwl in zip(sw, gw) if swl != gwl])
        return distance

    progress = True
    while progress:
        progress = False
        chain_items = len(chain)
        for i in range(chain_items):
            current_chain = chain.pop(0)
            # print(f'checking {current_chain} - {current_chain[-1]} - pool {usableWords}')
            for word in usableWords:
                possibles = usableWords[::1]
                for used in current_chain:
                    if used in possibles:
                        possibles.remove(used)
                        # print(f'possibles = {possibles}')

                if check_distance(current_chain[-1], word) == 1 and word in possibles:
                    progress = True
                    if word == goalWord:
                        solutions.append([*current_chain, word])
                    else:
                        chain.append([*current_chain, word])
                    # print(chain, usableWords)
    # find longest
    if len(solutions) == 0:
        return []
    longest = max([len(sol) for sol in solutions])
    sort_sol = [sol for sol in solutions if len(sol) == longest]
    # print(sort_sol)
    return sorted(sort_sol)[0]



# startWord = "code"
# goalWord = "dope"
# usableWords = ["cone",
#                "bonk",
#                "none",
#                "dole",
#                "tune",
#                "node",
#                "mode",
#                "nope",
#                "mole"]

# startWord= "functional"
# goalWord= "javascript"
# usableWords= ["incredible",
#  "programmer"]

startWord= "warm"
goalWord= "cold"
usableWords= ["care",
 "worm",
 "ward",
 "dare",
 "wore",
 "core",
 "bold",
 "bard",
 "cord",
 "card",
 "tare",
 "word",
 "ware",
 "bald",
 "gold"]


# startWord= "pink"
# goalWord= "ding"
# usableWords= ["dunk",
#  "donk",
#  "dunk",
#  "dank",
#  "punk",
#  "dung"]

# startWord= "abc"
# goalWord= "abc"
# usableWords= ["bbc"]


print(longestWordLadder(startWord, goalWord, usableWords))


