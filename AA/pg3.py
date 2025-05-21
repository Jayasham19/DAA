from collections import deque
def DFS(graph,start,visited=None):
    if visited is None:
        visited=set()
    print(start,end="")
    visited.add(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            DFS(graph,neighbour,visited)

def BFS(graph, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    q.append(neighbour)

graph = {
    'A': ['C', 'D','E'],
    'B': ['E', 'F'],
    'C': ['D', 'F'],
    'D': ['A','C'],
    'E': ['A','B','F'],
    'F': ['E']
}
DFS(graph,'A')
BFS (graph,'A')