def bfs(graph, start):
    visited = [False] * len(graph)
    queue = []
    queue.append(start)

    while not len(queue)==0:
        curr_node = queue.pop(0)
        visited[curr_node] = True
        print(f"Visiting node {curr_node}")
        for neighbour in graph[curr_node]:
            if not visited[neighbour] and neighbour not in queue:
                queue.append(neighbour)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1, 7],
    5: [2, 7],
    6: [2],
    7: [4, 5]
}
print("\nRunning BFS:")
bfs(graph, 0)