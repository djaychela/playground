def digitDegree(n):
    degree = 0
    while len(str(n))>1:
        ns = list(map(int,list(str(n))))
        n = sum(ns)
        degree+=1
    return degree

print(digitDegree(91))