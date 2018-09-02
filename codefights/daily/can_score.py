import itertools


def canScore(attacking_players, defending_players, d):
    pass


def calc_intersection(m, c, p, q, r):
    a = (m ** 2) + 1
    b = 2 * (m * c - m * q - p)
    c = q ** 2 - r ** 2 + p ** 2 - (2 * c * q) + c ** 2
    return (b ** 2 - (4 * a * c)) <= 0


def calc_slope(x1, y1, x2, y2):
    # TODO: catch if x1=x2
    m = (y1 - y2) / (x1 - x2)
    c = m * (0 - x1) + y1
    return m, c


def calc_intersection_2(x1, y1, x2, y2, p, q, r):
    if x1 == x2:
        if x1 <= p - r or x1 >= p + r:
            return True
        else:
            return False
    else:
        m = (y1 - y2) / (x1 - x2)
        cl = m * (0 - x1) + y1
        a = (m ** 2) + 1
        b = 2 * ((m * cl) - (m * q) - p)
        c = q ** 2 - r ** 2 + p ** 2 - (2 * cl * q) + cl ** 2
        print(m, cl, a, b, c)
        print(b ** 2 - (4 * a * c))
        return (b ** 2 - (4 * a * c)) <= 0


attacking_players = [[0, 0], [1, 2], [3, 3], [3, 1]]
defending_players = [[2, 1], [4, 4], [5, 5]]
radius = 1
for att in list(itertools.combinations(attacking_players, 2)):
    x1, y1 = att[0]
    x2, y2 = att[1]
    for defend in defending_players:
        def_x, def_y = defend
        print(att, defend)
        print(calc_intersection_2(x1, y1, x2, y2, def_x, def_y, radius))
    print('-----')

# print(calc_intersection(0, 1, 1, 0, 1))
# print(calc_slope(0,0, 1,2))
