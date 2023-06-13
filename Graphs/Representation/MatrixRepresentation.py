# # import numpy as np

# rows=3
# cols=4

# # matrix = np.zeros((rows, cols))
# # print(matrix)

# matrix = [[0] * cols for _ in range(rows)]

# for row in matrix:
#     print(row)

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest):
        if 0 <= src < self.vertices and 0 <= dest < self.vertices:
            self.adj_matrix[src][dest] = 1
            self.adj_matrix[dest][src] = 1

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)


# Example usage:
# graph = Graph(4)  # Create a graph with 4 vertices
# graph.add_edge(0, 1)  # Add an edge between vertex 0 and vertex 1
# graph.add_edge(0, 2)  # Add an edge between vertex 0 and vertex 2
# graph.add_edge(1, 3)  # Add an edge between vertex 1 and vertex 3
# graph.add_edge(2, 3)  # Add an edge between vertex 2 and vertex 3

# graph.print_adj_matrix()  # Print the adjacency matrix


# without class
def create_adjacency_matrix(vertices):
    adj_matrix = [[0] * vertices for _ in range(vertices)]
    return adj_matrix

def add_edge(adj_matrix, src, dest):
    if 0 <= src < len(adj_matrix) and 0 <= dest < len(adj_matrix):
        adj_matrix[src][dest] = 1
        adj_matrix[dest][src] = 1

def print_adjacency_matrix(adj_matrix):
    for row in adj_matrix:
        print(row)

# Example usage:
num_vertices = 4
adjacency_matrix = create_adjacency_matrix(num_vertices)

add_edge(adjacency_matrix, 0, 1)
add_edge(adjacency_matrix, 0, 2)
add_edge(adjacency_matrix, 1, 3)
add_edge(adjacency_matrix, 2, 3)

print_adjacency_matrix(adjacency_matrix)

