def matrixToDecimal_1(matrix):
    value = ''
    for i in range(len(matrix[0])):
        current_line = ''
        for j in range(len(matrix)):
            current_line += matrix[j][i]
        current_line_value = 0
        if current_line[0] == '|':
            current_line_value += 5
        for i in range(5):
            if current_line[3 + i] == '|':
                current_line_value += i
        value += str(current_line_value)
        if current_line[2] == '.':
            value += '.'

    return float(value)


def matrixToDecimal(m):
    v = ''
    for i in range(len(m[0])):
        cl = 0
        dec = False
        for j in range(8):
            d = m[j][i]
            if d == '.':
                dec = True
            elif d == '|':
                if j == 0:
                    cl += 5
                if j >= 4:
                    cl += j - 3
        v += str(cl)
        if dec:
            v += '.'

    return float(v)


# matrix = [["o","o","o","|","|","o"],
#  ["|","|","|","o","o","|"],
#  ["-","-",".","-","-","-"],
#  ["|","|","o","o","o","o"],
#  ["o","o","|","o","|","o"],
#  ["o","o","o","o","o","o"],
#  ["o","o","o","o","o","|"],
#  ["o","o","o","|","o","o"]]


matrix = [["o", "o", "o", "|", "|"],
          ["|", "|", "|", "o", "o"],
          ["-", "-", ".", "-", "-"],
          ["o", "|", "|", "o", "|"],
          ["o", "o", "o", "|", "o"],
          ["o", "o", "o", "o", "o"],
          ["|", "o", "o", "o", "o"],
          ["o", "o", "o", "o", "o"]]

print(matrixToDecimal(matrix))
