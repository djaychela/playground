def sudoku(grid):
    if False in [sorted(grid[i]) == list(range(1, 10)) for i in range(9)]:
        return False
    if False in [sorted([grid[j][i] for j in range(9)]) == list(range(1, 10)) for i in range(9)]:
        return False
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            temp_grid = sorted([grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3)])
            if temp_grid != list(range(1, 10)):
                return False
    return True


def sudoku_2(grid):
    def check_all(list):
        for i in range(1, 10):
            if i not in list:
                return False
        return True

    for i in range(9):
        if not check_all(list(set(grid[i]))):
            return False
    for i in range(9):
        vert = [grid[j][i] for j in range(9)]
        if not check_all(vert):
            return False

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            temp_grid = []
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    temp_grid.append(grid[i][j])
            if not check_all(temp_grid):
                return False
    return True


print(sudoku([[1, 3, 2, 5, 4, 6, 9, 2, 7],
              [4, 6, 5, 8, 7, 9, 3, 8, 1],
              [7, 9, 8, 2, 1, 3, 6, 5, 4],
              [9, 2, 1, 4, 3, 5, 8, 7, 6],
              [3, 5, 4, 7, 6, 8, 2, 1, 9],
              [6, 8, 7, 1, 9, 2, 5, 4, 3],
              [5, 7, 6, 9, 8, 1, 4, 3, 2],
              [2, 4, 3, 6, 5, 7, 1, 9, 8],
              [8, 1, 9, 3, 2, 4, 7, 6, 5]]))

print(sudoku([[1, 3, 2, 5, 4, 6, 9, 8, 7],
              [4, 6, 5, 8, 7, 9, 3, 2, 1],
              [7, 9, 8, 2, 1, 3, 6, 5, 4],
              [9, 2, 1, 4, 3, 5, 8, 7, 6],
              [3, 5, 4, 7, 6, 8, 2, 1, 9],
              [6, 8, 7, 1, 9, 2, 5, 4, 3],
              [5, 7, 6, 9, 8, 1, 4, 3, 2],
              [2, 4, 3, 6, 5, 7, 1, 9, 8],
              [8, 1, 9, 3, 2, 4, 7, 6, 5]]))
