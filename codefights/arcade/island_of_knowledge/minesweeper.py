def minesweeper(matrix):
    x_size = len(matrix)
    y_size = len(matrix[0])
    print(x_size, y_size)
    output=[]
    for i in range (x_size):
        current_row=[]
        for j in range(y_size):
            print(f'cell:{i}:{j}')
            cell_total = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0 <= i+x <= x_size-1 and 0 <= j+y <= y_size-1 and not i+x==j+x==0:
                        print(i, j, x, y, i + x, j + y)
                        if matrix[i+x][j+y]:

                            cell_total += 1

            current_row.append(cell_total)

        output.append(current_row)
    return output


true = True
false = False
# print(minesweeper([[true, false, false],
#           [false, true, false],
#           [false, false, false]]))

print(minesweeper([[true,false,false,true],
 [false,false,true,false],
 [true,true,false,true]]))