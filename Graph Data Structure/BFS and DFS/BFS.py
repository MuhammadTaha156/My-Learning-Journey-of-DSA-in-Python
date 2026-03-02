from collections import deque

def BFS(graph, start):
    # Step 1: Create visited dictionary
    visited = {vertex: False for vertex in graph}

    # Step 2: Create queue
    Q = deque()

    # Step 3: Insert start node
    Q.append(start)
    visited[start] = True

    print("BFS Traversal:", end=" ")

    # Step 4: While queue is not empty
    while Q:
        # Get front node
        n = Q.popleft()
        print(n, end=" ")

        # Visit all neighbors of n
        for u in graph[n]:
            if visited[u] == False:
                Q.append(u)
                visited[u] = True
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

BFS(graph, 0)
