def chessBoardCellColor(cell1, cell2):
    cell_color_1 = chessboard_offset(cell1[0]) + int(cell1[1]) % 2
    cell_color_2 = chessboard_offset(cell2[0]) + int(cell2[1]) % 2
    return cell_color_1 == cell_color_2


def chessboard_offset(letter):
    if letter in 'aceg':
        return 1
    return 0


def chessBoardCellColor_2(cell1, cell2):
    cell_color_1 = ((1 if cell1[0].lower() in 'aceg' else 0) + int(cell1[1])) % 2
    cell_color_2 = ((1 if cell2[0].lower() in 'aceg' else 0) + int(cell2[1])) % 2
    print(cell_color_1, cell_color_2)
    return cell_color_1 == cell_color_2


print(chessBoardCellColor_2('a1','b2'))

for i in range (1,8):
    print(i, i %2)
