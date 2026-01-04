from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

bfs(graph, 0)
