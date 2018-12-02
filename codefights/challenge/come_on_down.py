def comeOnDown(m, b):
    g = 0
    bp = 0
    p = m
    b.append(m + 1)
    b.append(0)
    all_bids = sorted(b, reverse=True)
    for pr in all_bids:
        if pr > m+1:
            continue
        tg = p - pr
        print(f'price = {pr}, gap = {tg}')
        if tg >= g:
            g = tg
            bp = pr
        p = pr
    return bp + 1


# print(comeOnDown(maxPrice=8, bids=[9, 10, 11]))
# print(comeOnDown(maxPrice=8, bids=[1, 2, 3, 4]))

print(comeOnDown(m=9, b=[1, 5, 10]))

# bids = [2599, 972, 700, 2013]
# maxprice = 3250

bids = [15, 57, 36, 250]
maxprice = 75

# bids = [5000, 3500, 7250, 8999]
# maxprice = 10000
print(comeOnDown(maxprice, bids))
