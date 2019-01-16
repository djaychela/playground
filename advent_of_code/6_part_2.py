data = """59, 110
127, 249
42, 290
90, 326
108, 60
98, 168
358, 207
114, 146
242, 170
281, 43
233, 295
213, 113
260, 334
287, 260
283, 227
328, 235
96, 259
232, 177
198, 216
52, 115
95, 258
173, 191
156, 167
179, 135
235, 235
164, 199
248, 180
165, 273
160, 297
102, 96
346, 249
176, 263
140, 101
324, 254
72, 211
126, 337
356, 272
342, 65
171, 295
93, 192
47, 200
329, 239
60, 282
246, 185
225, 324
114, 329
134, 167
212, 104
338, 332
293, 94"""

# data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""

data = data.split('\n')


def get_data():
    global data
    return data


def find_biggest_coord(data):
    highest = 0
    for d in data:
        x, y = d.split(',')
        x = int(x)
        y = int(y)
        this_max = max(x, y)
        highest = max(highest, this_max)
    return highest


def place_coords(grid, data, offset):
    for idx, d in enumerate(data, 1):
        x, y = d.split(',')
        x = int(x) + offset
        y = int(y) + offset
        grid[x][y] = 2 ** idx
    return grid


def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for i in range(height):
        line = ''
        for j in range(width):
            line += f'{grid[i][j]:>1}'
        print(line)


def calc_manhattan(grid, offset, threshold):
    width = len(grid[0])
    height = len(grid)
    # calculate manhattan distance for each grid location
    for i in range(width):
        for j in range(width):
            total_dist = 0
            for idx, d in enumerate(data, 1):
                x, y = d.split(',')
                x = int(x) + offset
                y = int(y) + offset
                dist = abs(i - x) + abs(j - y)
                total_dist += dist
            if total_dist < threshold:
                grid[i][j] = 1
    return grid


def calc_areas(grid):
    width = len(grid[0])
    height = len(grid)
    # calculate areas of each power of 2
    totals = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                totals += 1
    return totals


def main():
    original_size = find_biggest_coord(get_data()) + 2

    scores_list = []

    threshold = 10000

    width = original_size
    height = original_size
    offset = 0

    grid = [[0 for _ in range(width)] for _ in range(height)]

    data = get_data()

    # grid = place_coords(grid, data, offset)
    # print_grid(grid)

    print()

    grid = calc_manhattan(grid, offset, threshold)
    print_grid(grid)

    scores_list.append(calc_areas(grid))

    print(scores_list)


if __name__ == '__main__':
    main()
