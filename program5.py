Q5) Write a program to implement Breadth First Search Traversal
from collections import defaultdict, deque

class Graph:
def _init_(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

# Example usage:
if __name__ == "_main_":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    start_vertex = 2
    bfs_result = g.bfs(start_vertex)

print(f"Breadth-First Traversal starting from vertex {start_vertex}:")
    print(bfs_result)
