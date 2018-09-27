def mapDecoding(message):
    dp = [0 for l in range(len(message))]
    dp.append(1)
    dp.append(1)
    limit = 1e9 + 7

    for i in range(len(message)-1, -1, -1):
        one_digit = int(message[i])

        if one_digit == 0:
            dp[i] = 0;
            continue

        # use single digit number
        total = dp[i+1]

        # what about double digit number
        if i < len(message) - 1:
            two_digit = one_digit * 10 + int(message[i + 1])
            if two_digit <= 26:
                total += dp[i+2]

        dp[i] = int(total % limit)

    return dp[0]




print(mapDecoding('123'))
print(mapDecoding("11115112112"))

