from collections import deque

def topological_sort(graph):
    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque()
    for u in indegree:
        if indegree[u] == 0:
            q.append(u)

    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return topo

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

print(topological_sort(graph))
