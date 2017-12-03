t = int(input().strip())
for a0 in range(t):
    n = input().strip()
    print(len([i for i in map(int, list(n)) if i != 0 and int(n) % i == 0]))

