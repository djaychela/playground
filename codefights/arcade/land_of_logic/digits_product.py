def digitsProduct(product):
    i = product
    for i in range (1, (product*20) + 12):
        current = list(map(int, list(str(i))))
        sum = 1
        for digit in current:
            sum = sum * digit

        if sum == product:
            output = 0
            for digit in current:
                output = output * 10 + digit

            return output

    return -1


print(digitsProduct(1))
