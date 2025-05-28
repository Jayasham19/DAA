def dijkstra(graph):
    n = len(graph)
    dist = [999] * n
    visited = [False] * n
    prev = [-1] * n
    dist[0] = 0

    for _ in range(n):
        min_val = 999
        u = 0
        for i in range(n):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                u = i

        visited[u] = True

        for e in graph[u]:
            v = e[0]
            w = e[1]
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    for i in range(n):
        p = []
        x = i
        while x != -1:
            p.insert(0, x)
            x = prev[x]
        print("Path to", i, ":", p, "Distance:", dist[i])
# Driver code
graph = {
    0: [[3, 7]],
    1: [[2, 4]],
    2: [[4, 6]],
    3: [[1, 2], [2, 5]],
    4: [[3, 4]]
}

dijkstra(graph)




