class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, src, dest):
        if 0 <= src < self.vertices and 0 <= dest < self.vertices:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)

    def print_adj_list(self):
        for vertex in range(self.vertices):
            print(f"Adjacency list of vertex {vertex}: ", end="")
            for neighbor in self.adj_list[vertex]:
                print(f"{neighbor} -> ", end="")
            print("None")

# Example usage:
graph = Graph(4)  # Create a graph with 4 vertices
graph.add_edge(0, 1)  # Add an edge between vertex 0 and vertex 1
graph.add_edge(0, 2)  # Add an edge between vertex 0 and vertex 2
graph.add_edge(1, 3)  # Add an edge between vertex 1 and vertex 3
graph.add_edge(2, 3)  # Add an edge between vertex 2 and vertex 3

graph.print_adj_list()  # Print the adjacency list
