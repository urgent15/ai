def dfs(graph, node, visited):
    if visited[node]:
        return
    else:
        print(f"Visiting node {node}")
        visited[node] = 1
        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs(graph, neighbour, visited)

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

visited = [0] * len(graph)
print("Running DFS:")
dfs(graph, 0, visited)