def queens_attack_2(board_size, queen_position, *args):
    moves = 0
    # create the board
    board_line = [0] * board_size
    board = []
    for i in range(board_size):
        board.append(board_line.copy())
    # place the pieces
    board[queen_position[0]-1][queen_position[1]-1] = 'q'
    for arg in args:
        board[arg[0]-1][arg[1]-1] = 'x'
    print('*** Starting Board ***')
    print_board(board)
    print('*** moves ***')
    # check horizontal movement
    current_x, current_y = queen_position
    current_x -= 1
    current_y -= 1
    current_x += 1
    while str(board[current_x][current_y]) not in 'xq' and current_x < board_size-1:
        print(current_x, current_y)
        if board[current_x][current_y] == 0:
            board[current_x][current_y] = '*'
        current_x += 1
        if board[current_x][current_y] == 0:
            moves +=1

    # need method of vector addition!!!

    # start at queen position
    # move to right until hit something
    # start at queen position
    # move to left until hit something
    # etc

    # check vertical movement
    # check diagonal movement /
    # check diagonal movement \
    print_board(board)
    return moves


def print_board(chessboard):
    for line in chessboard:
        output = ''
        for element in line:
            output = output + str(element) + ' '
        print(output)


print(queens_attack_2(8, (4, 3), (5, 5), (4, 2), (2, 3)))