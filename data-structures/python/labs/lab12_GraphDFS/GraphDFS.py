from collections import defaultdict


class Graph:
    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, vertex1, vertex2):
        """Function to add an edge to the graph from vertex1 to vertex2"""
        self.graph[vertex1].append(vertex2)

    def dfs_util(self, node, visited):
        """Utility function used by DFS."""
        # print the current node and add it to visited set
        print(node, end=" ")
        visited.add(node)

        # recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, node):
        """Prints DFS traversal of a graph given a starting node."""
        # create a set to store all visited vertices
        visited = set()

        # call the recursive helper function to print DFS traversal
        self.dfs_util(node, visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    print("Depth First Traversal")
    graph.dfs(0)
