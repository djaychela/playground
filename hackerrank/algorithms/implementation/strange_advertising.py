def strange_advertising(days):
    viewers = 5
    total_viewers = 0
    for i in range(1, days+1):
        viewers = viewers // 2
        total_viewers += viewers
        viewers = viewers * 3

    return total_viewers


print(strange_advertising(3))
print(strange_advertising(24))
#
# n = int(input())
# shared = 5
# total_opened = 0
#
# for _ in range(0, n):
#     opened = int(shared / 2)
#     total_opened = total_opened + opened
#     shared = opened * 3
#
# print(total_opened)