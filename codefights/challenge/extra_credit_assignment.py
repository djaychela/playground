def extraCreditAssignment(dec, den):
    ds = dec.split('(')[0]
    try:
        dr = dec.split('(')[1]
    except IndexError:
        dr = '0'
    dr = dr.strip(')')
    for i in range(20):
        ds += dr

    return round(float(ds) * den)




# decimal= "0.(3)"
# denominator= 3

# decimal= "4.6"
# denominator= 5

decimal= "12.40(789473684210526315)"
denominator= 76
# should give 943?

# decimal= "1.0(4811715)"
# denominator= 478
# # should give 501?


print(extraCreditAssignment(decimal, denominator))