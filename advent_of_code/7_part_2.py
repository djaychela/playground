import string

data = """Step B must be finished before step G can begin.
Step G must be finished before step J can begin.
Step J must be finished before step F can begin.
Step U must be finished before step Z can begin.
Step C must be finished before step M can begin.
Step Y must be finished before step I can begin.
Step Q must be finished before step A can begin.
Step N must be finished before step L can begin.
Step O must be finished before step A can begin.
Step Z must be finished before step T can begin.
Step I must be finished before step H can begin.
Step L must be finished before step W can begin.
Step F must be finished before step W can begin.
Step T must be finished before step X can begin.
Step A must be finished before step X can begin.
Step K must be finished before step X can begin.
Step S must be finished before step P can begin.
Step M must be finished before step E can begin.
Step E must be finished before step W can begin.
Step D must be finished before step P can begin.
Step P must be finished before step W can begin.
Step X must be finished before step H can begin.
Step V must be finished before step W can begin.
Step R must be finished before step H can begin.
Step H must be finished before step W can begin.
Step N must be finished before step I can begin.
Step X must be finished before step R can begin.
Step D must be finished before step V can begin.
Step V must be finished before step R can begin.
Step F must be finished before step K can begin.
Step P must be finished before step R can begin.
Step P must be finished before step V can begin.
Step S must be finished before step X can begin.
Step I must be finished before step S can begin.
Step J must be finished before step N can begin.
Step T must be finished before step S can begin.
Step T must be finished before step R can begin.
Step K must be finished before step P can begin.
Step N must be finished before step R can begin.
Step G must be finished before step T can begin.
Step I must be finished before step V can begin.
Step G must be finished before step Q can begin.
Step D must be finished before step H can begin.
Step V must be finished before step H can begin.
Step T must be finished before step K can begin.
Step T must be finished before step W can begin.
Step E must be finished before step H can begin.
Step C must be finished before step R can begin.
Step L must be finished before step K can begin.
Step G must be finished before step Y can begin.
Step Y must be finished before step O can begin.
Step O must be finished before step E can begin.
Step U must be finished before step S can begin.
Step X must be finished before step W can begin.
Step C must be finished before step D can begin.
Step E must be finished before step P can begin.
Step B must be finished before step R can begin.
Step F must be finished before step R can begin.
Step A must be finished before step D can begin.
Step G must be finished before step M can begin.
Step B must be finished before step Q can begin.
Step Q must be finished before step V can begin.
Step B must be finished before step W can begin.
Step S must be finished before step H can begin.
Step P must be finished before step X can begin.
Step I must be finished before step M can begin.
Step A must be finished before step S can begin.
Step M must be finished before step X can begin.
Step L must be finished before step S can begin.
Step S must be finished before step W can begin.
Step L must be finished before step V can begin.
Step Z must be finished before step X can begin.
Step M must be finished before step R can begin.
Step T must be finished before step A can begin.
Step N must be finished before step V can begin.
Step M must be finished before step H can begin.
Step E must be finished before step D can begin.
Step F must be finished before step V can begin.
Step B must be finished before step O can begin.
Step G must be finished before step U can begin.
Step J must be finished before step C can begin.
Step G must be finished before step F can begin.
Step Y must be finished before step M can begin.
Step F must be finished before step D can begin.
Step M must be finished before step P can begin.
Step F must be finished before step T can begin.
Step G must be finished before step A can begin.
Step G must be finished before step Z can begin.
Step K must be finished before step V can begin.
Step J must be finished before step Z can begin.
Step O must be finished before step Z can begin.
Step B must be finished before step E can begin.
Step Z must be finished before step V can begin.
Step Q must be finished before step O can begin.
Step J must be finished before step D can begin.
Step Y must be finished before step E can begin.
Step D must be finished before step R can begin.
Step I must be finished before step F can begin.
Step M must be finished before step V can begin.
Step I must be finished before step D can begin.
Step O must be finished before step P can begin."""

# data = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin."""


other = [[] for i in range(26)]
nodes = list(string.ascii_uppercase)
time = [["." for i in range(5)] for j in range(1700)]
lines = []

data=data.split('\n')

for line in data:
    cond = line.split(" ")[1]
    targ = nodes.index(line.split(" ")[7])
    other[targ].append(cond)

let = ""

vis = [False for i in range(26)]  # changed
for i, tim in enumerate(time):
    j = 0
    while j < len(other):
        complete = False
        let = nodes[j]

        if len(other[j]) == 0 and not let in tim:

            for l, work in enumerate(tim):
                if i - 1 >= 0:
                    if time[i - 1][l] == let:
                        other[j] = [0]

                        for k, anot in enumerate(other):
                            other[k] = list(filter((nodes[j]).__ne__, anot))
                            complete = True
                        break

                if work == "." and not vis[nodes.index(let)]:  # changed
                    temp = i + j + 61
                    vis[nodes.index(let)] = True  # changed
                    for m in range(i, temp):
                        time[m][l] = let

                    break

            if complete:
                j = -1

        j += 1

print(time.index([".", ".", ".", ".", "."]))