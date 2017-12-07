import datetime


def library_fine(d1,m1,y1,d2,m2,y2):
    actual = datetime.date(y1, m1, d1)
    expected = datetime.date(y2, m2, d2)
    over = actual - expected
    if over.days <=0:
        return 0
    if y1 - y2 >= 1:
        return 10000
    if m1 - m2 >=1:
        return 500 * (m1 - m2)
    if d1 - d2 >=1:
        return 15 * (d1 - d2)
    return 0


print(library_fine(9,6,2015,6,6,2015))
print(library_fine(2,7,1014,1,1,1015))
