import itertools


def latticevillePaths(m, n):
    def trace_path(current_route):
        pos_x = 0
        pos_y = m - 1
        lattice[pos_y][pos_x] = 1
        for move in current_route:
            if move == 'n':
                pos_y -= 1
            if move == 'e':
                pos_x += 1
            lattice[pos_y][pos_x] = 1
        score = sum(map(sum, lattice))
        # print(f'complete: {current_route} - map: {lattice} - score: {score}')
        return score

    north = ['n' for _ in range(m - 1)]
    east = ['e' for _ in range(n - 1)]
    path = north + east
    routes = list(set(itertools.permutations(path)))
    route_sets = list(set(itertools.combinations(routes, 2)))
    high_score = 0
    high_score_tally = 0
    for routes in route_sets:
        lattice = [[0] * n for _ in range(m)]
        current_route = routes[0]
        trace_path(current_route)
        current_route = routes[1]
        current_route_score = trace_path(current_route)
        if current_route_score > high_score:
            high_score = current_route_score
            high_score_tally = 0
        if current_route_score == high_score:
            high_score_tally +=1

    return high_score_tally % ((10**9)+7)


for i in range(1,8):
    for j in range(2,8):
        print(f'For {i}*{j} : {latticevillePaths(i, j)}')
