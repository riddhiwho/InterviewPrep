from collections import deque

def bfs(graph, start):
    visited = [False]*len(graph)
    queue = deque()
    
    visited[start] = True
    queue.append(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        #enqueue all the neighbors of the popped vertex that haven't been visited
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)
    

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

start_vertex = 0
bfs(graph, start_vertex)

