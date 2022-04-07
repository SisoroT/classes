from collections import defaultdict


class Graph:
    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, vertex1, vertex2):
        """Function to add an edge to the graph from vertex1 to vertex2"""
        self.graph[vertex1].append(vertex2)

    def bfs(self, node):
        """Prints BFS traversal of a graph given a starting node."""
        # create a set to store all visited vertices
        visited = set()

        # create a queue for BFS
        queue = []

        # enqueue the source node and mark the it as visited
        queue.append(node)
        visited.add(node)

        while queue:

            # dequeue a node from the queue and print it
            node = queue.pop(0)
            print(node, end=" ")

            # if an adjacent node hasn't been visited,
            # enqueue it and mark it visited
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


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
    graph.bfs(0)
