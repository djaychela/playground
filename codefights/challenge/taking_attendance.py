def takingAttendance(c):
    t = 0
    for name in c:
        t += 5
        s = 0
        for l in name.lower():
            if l not in 'aeiouy':
                if s == 0:
                    s = 1
                else:
                    s *= 2
            else:
                t += s
                s = 0
        t += s
    return t





print(takingAttendance(["Ashley",
 "Robert",
 "Miles",
 "Archibald",
 "Taylor",
 "Vanessa",
 "Isaac"]))

# ,
#  "Robert",
#  "Miles",
#  "Archibald",
#  "Taylor",
#  "Vanessa",
#  "Isaac"]))
