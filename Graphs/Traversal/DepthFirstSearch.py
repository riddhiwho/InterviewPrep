def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

start_vertex = 0
visited = [False]*len(graph)

dfs(graph, start_vertex, visited)