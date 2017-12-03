def circular_array_rotation(array, rotation, queries):
    index = rotation % len(array)
    print(index)
    for query in queries:
        print(query-index, ((query-index) % len(array)))
        print(array[(query - index) % len(array)])


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
queries = []
for a0 in range(q):
    m = int(input().strip())
    queries.append(m)
circular_array_rotation(a,m,queries)