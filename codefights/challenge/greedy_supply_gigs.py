def greedySupplyGigs(offers):
    total = 0
    schools_taken = {}
    schools_reject = {}
    for day in offers:
        today_school = ''
        today_pay = 0
        rejected = []
        print(day)
        for offer in day:
            details = offer.split()
            school = details[0]
            pay = int(details[1][1:])
            print(school, pay)
            if school not in schools_reject.keys():
                schools_reject[school] = 0
            if school not in schools_taken.keys():
                schools_taken[school] = 0
            if schools_reject[school] <= schools_taken[school] / 2:
                if pay <= today_pay:
                    print(f'school:{school} less than reject {rejected}')
                    rejected.append(school)
                if pay > today_pay:
                    today_pay = pay
                    rejected.append(today_school)
                    today_school = school
        if today_school in schools_taken.keys():
            schools_taken[today_school] += 1
        else:
            schools_taken[today_school] = 1
        for reject in rejected:
            if reject in schools_reject.keys():
                schools_reject[reject] += 1
            else:
                schools_reject[reject] = 1
        total += today_pay
        print(f'today_school:{today_school}, today_pay: {today_pay}')
        print(f'rejected:{rejected}')
    print(schools_reject, schools_taken)

    return total


# offers = [["A $100", "B $200", "C $150"]]
# # 200
#
# offers = [["A $100", "B $200"],
#           ["A $250"],
#           ["A $200"]]
# # 200

offers= [["V $75","H $100","P $100"],
 ["F $100"],
 ["P $150"],
 ["H $75"],
 ["R $150","F $250","C $125","X $150","P $200","Q $150"],
 ["B $125"],
 ["F $150","B $75","H $75"],
 ["D $200","X $175","C $125","B $250"],
 ["R $150","V $125","D $200"],
 ["H $250"]]



print(greedySupplyGigs(offers))
