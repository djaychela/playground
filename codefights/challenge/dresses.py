def dresses(c):
    o = []
    for idx, t in enumerate(c):
        r = int(t[:2], 16)
        g = int(t[2:4], 16)
        b = int(t[4:],16)
        if g > b and g > r:
            o.append(idx)
    return o

def dresses_2(c):
    o = []
    for idx, t in enumerate(c):
        r = t[:2]
        g = t[2:4]
        b = t[4:]
        if g > b and g > r:
            o.append(idx)
    return o


colors= ["A0FC77", "90CACA"]
print(dresses_2(colors))
colors= ["000000", "101110", "F01AC3", "0FFEF4"]
print(dresses_2(colors))