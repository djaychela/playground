def differentSquares(matrix):
    height = len(matrix)
    width = len(matrix[0])
    all_squares = []
    for i in range(height - 1):
        for j in range(width - 1):
            current_matrix=[[0,0],[0,0]]
            for k in range(2):
                for l in range(2):
                    current_matrix[k][l] = matrix[i+k][j+l]
            if current_matrix not in all_squares:
                all_squares.append(current_matrix)
    return len(all_squares)




matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

print(differentSquares(matrix))