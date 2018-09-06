def countBits(n):
    print(bin(n)[2:])
    return len(bin(n)[2:])



print(countBits(50))