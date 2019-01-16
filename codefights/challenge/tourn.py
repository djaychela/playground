def bfsDistancesUnweightedGraph(matrix, startVertex):

    visited = []
    queue = []
    distance = []

    for i in range(len(matrix)):
        visited.append(False)
        distance.append(0)



    visited[startVertex] = True
    queue.append(startVertex)

    print(visited, distance, queue)
    while len(queue) > 0:
        currentVertex = queue[0]
        queue = queue[1:]
        visited[currentVertex] = True
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                distance[nextVertex] = distance[currentVertex] + 1
                queue.append(nextVertex)
                print(visited, distance, queue)
    return distance


matrix= [[False,False,True],
 [False,False,True],
 [True,True,False]]
startVertex= 0

print(bfsDistancesUnweightedGraph(matrix, startVertex))