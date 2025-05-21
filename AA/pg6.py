def floyd_warshall(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
def transitive_closure(reach, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
INF = 100
graph = [
    [0, 10, 3, INF],
    [INF, 0, INF, 2],
    [INF, 4, 0, 8],
    [INF, INF, INF, 0]
]

n = len(graph)
floyd_warshall(graph, n)

print("All-Pairs Shortest Paths (Floyd-Warshall):")
for row in graph:
    print(row)
graph = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

n = len(graph)
transitive_closure(graph, n)

print("Transitive Closure (Warshall's Algorithm):")
for row in graph:
    print(row)
