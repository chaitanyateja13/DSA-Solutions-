def detect_cycle(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if detect_cycle(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True
    return False

graph = {
    0: [1],
    1: [0, 2],
    2: [1]
}

visited = set()
print(detect_cycle(graph, 0, visited, -1))
