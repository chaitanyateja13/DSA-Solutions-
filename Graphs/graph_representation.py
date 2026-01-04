# Adjacency List representation
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

print(graph)

# Adjacency Matrix representation
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]

for row in matrix:
    print(row)
