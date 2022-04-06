from collections import defaultdict


class Graph:
    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, vertex1, vertex2):
        """Function to add an edge to the graph from vertex1 to vertex2"""
        self.graph[vertex1].append(vertex2)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    print("Breadth First Traversal")
    # graph.bfs(0)
