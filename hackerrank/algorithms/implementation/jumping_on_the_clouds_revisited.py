n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
e = 100
cloud = 0
running = True
while running:
    cloud = (cloud + k) % n
    e -= 1 + (2 * c[cloud])
    if cloud == 0:
        running = False
print(e)

