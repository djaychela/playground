def bomber(field):
    if len(field) == 0:
        return 0
    if len(field[0]) == 0:
        return 0
    height = len(field)
    width = len(field[0])
    result = [[0 for h in range(width)] for w in range(height)]
    # how many enemies in each row?
    for i in range(height):
        col_stack = []
        enemies = 0
        for j in range(width):
            tile = field[i][j]
            if tile == 'E':
                enemies += 1
            elif tile == '0':
                col_stack.append(j)
            elif tile == 'W':
                # hit a wall, empty the stack
                while len(col_stack) > 0:
                    # print(col_stack)
                    result[i][col_stack.pop()] += enemies
                enemies = 0
        # hit the edge, empty the stack.
        # print(f'hit the edge - colstack {col_stack}, i={i}, j={j}')
        while len(col_stack) > 0:
            result[i][col_stack.pop()] += enemies
            # print(result)

    # how many enemies in each column?
    for j in range(width):
        row_stack = []
        enemies = 0
        for i in range(height):

            tile = field[i][j]
            if tile == 'E':
                enemies += 1
            elif str(tile).isdigit():
                row_stack.append(i)
            elif tile == 'W':
                # hit a wall, empty the stack
                while len(row_stack) > 0:

                    result[row_stack.pop()][j] += enemies
                enemies = 0
        # hit the edge, empty the stack.
        while len(row_stack) > 0:
            result[row_stack.pop()][j] += enemies
    return max(map(max, result))


def bomber_brute(field):
    max_score = 0
    if len(field) == 0:
        return 0
    height = len(field)
    width = len(field[0])
    for x in range(height):
        for y in range(width):
            if field[x][y] == '0':
                enemies = 0
                for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    # print(x, y, dx, dy)
                    i = 1
                    while i < 100:
                        next_x, next_y = x + i * dy, y + i * dy
                        if 0 < next_x < height and 0 < next_y < width:
                            if field[next_x][next_y] != 'W':
                                if field[next_x][next_y] == 'E':
                                    enemies += 1
                                    print(next_x, next_y, enemies, field[next_x][next_y])
                        else:
                            i = 101
                        i += 1

                max_score = max(enemies, max_score)

    return max_score

#
# field = [["0", "0", "E", "0"],
#          ["W", "0", "W", "E"],
#          ["0", "E", "0", "W"],
#          ["0", "W", "0", "E"]]

# field = [["0","E","0","0"],
#  ["E","0","W","E"],
#  ["0","E","0","0"]]

field = [["E"],
 ["E"],
 ["E"]]

print(bomber(field))

# [1, 1, 'E', 1], ['W', 0, 'W', 'E'], [1, 'E', 1, 'W'], [0, 'W', '0', 'E']] is correct after first run (rows)

# field = []
#
# print(bomber(field))
