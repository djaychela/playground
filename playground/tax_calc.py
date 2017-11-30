def calc_tax_due(amount, allowance_used):
    tax_amount = 0
    lower_rate = 0.2
    higher_rate = 0.4
    additional_rate = 0.45

    if amount < 11500 and not allowance_used:
        return 0
    elif amount < 11500 and allowance_used:
        return amount * lower_rate
    elif amount >= 11500 and not allowance_used:
        amount -= 11500
    else:
        tax_amount += (11500 * lower_rate)
        amount -= 11500

    if amount > 33500:
        tax_amount += (33500 * lower_rate)
        amount -= 33500
    else:
        tax_amount += (amount * lower_rate)
        return tax_amount

    if amount > 105000:
        tax_amount += (105000 * higher_rate)
        amount -= 105000
    else:
        tax_amount += (amount * higher_rate)
        return tax_amount
    tax_amount += (amount * additional_rate)
    return tax_amount


for i in range(0,700000, 10000):
    print(f"Value: {i},  after tax: {i- calc_tax_due(i, True)}")

