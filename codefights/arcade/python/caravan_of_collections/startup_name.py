def startupName(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    # res = cmp1.intersection(cmp2).intersection(cmp3).symmetric_difference(cmp1.symmetric_difference(cmp2).symmetric_difference(cmp3))
    res = cmp1.union(cmp2).union(cmp3).symmetric_difference(cmp1.symmetric_difference(cmp2).symmetric_difference(cmp3))
    return list(sorted(list(res)))


companies = ["coolcompany", "nicecompany", "legendarycompany"]
print(startupName(companies))