def dfs(graph, start):
    visited = set()
    stack = []

    stack.append(start)
    visited.add(start)

    while stack:
        node = stack.pop()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
dfs(graph, 0)