def bishopAndPawn(bishop, pawn):
    bishop_alpha = ord(bishop[0])-96
    bishop_num = int(bishop[1])
    pawn_alpha = ord(pawn[0])-96
    pawn_num = int(pawn[1])
    if (bishop_alpha + bishop_num) == (pawn_alpha + pawn_num):
        return True
    bishop_alpha = 9 - bishop_alpha
    pawn_alpha = 9 - pawn_alpha
    if (bishop_alpha + bishop_num) == (pawn_alpha + pawn_num):
        return True
    return False



print(bishopAndPawn('a3','b2'))