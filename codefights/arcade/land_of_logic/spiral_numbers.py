def spiralNumbers(n):
    coord = [0, -1]
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    val = 1
    dir_ptr = 0
    ctr = 1  # set for first time
    output = [[0 for _ in range(n)] for _ in range(n)]
    current = 0
    while n > 0:
        while current < n:
            coord[0] += dirs[dir_ptr][0]
            coord[1] += dirs[dir_ptr][1]
            output[coord[0]][coord[1]] = val
            val += 1
            current += 1
        ctr += 1
        if ctr == 2:
            n -= 1
            ctr = 0
        current = 0
        dir_ptr += 1
        if dir_ptr > 3:
            dir_ptr = 0
    return output


print(spiralNumbers(5))
