Q6)Write a program to implement Depth First Search Traversal.
from collections import defaultdict

class Graph:
def _init_(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        print("Depth-First Traversal:")
        self.dfs_util(start, visited)

# Example usage:
if __name__ == "_main_":
    g = Graph()
    g.add_edge (0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    start_vertex = 2
g.dfs(start_vertex)
