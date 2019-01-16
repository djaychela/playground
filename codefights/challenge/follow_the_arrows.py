def followTheArrows(dmap, start):
    y = start[0]
    x = start[1]
    sy = len(dmap)
    sx = len(dmap[0])
    vecs = {'>': [0, 1], '<': [0, -1], 'v': [1, 0], '^': [-1, 0], '.': [200, 200]}
    running = True
    while running:
        move = vecs[dmap[y][x]]
        this_line = dmap[y]
        new_line = ''.join([char if idx != x else '.' for idx, char in enumerate(this_line)])
        dmap[y] = new_line
        y += move[0]
        x += move[1]
        if 0 > x or x >= sx or 0 > y or y >= sy:
            running = False

    return dmap


directionMap = [">>",
                ">v",
                "^<"]
start = [0, 0]

print(followTheArrows(directionMap, start))
