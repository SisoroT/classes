import java.util.*;

// Class representing a directed graph using adjacency lists
class Graph {
    int V; // Number of Vertices
    LinkedList<Integer>[] adj; // adjacency lists

    // Constructor
    Graph(int V) {
        this.V = V;
        adj = new LinkedList[V];

        for (int i = 0; i < adj.length; i++)
            adj[i] = new LinkedList<Integer>();
    }

    // To add an edge to graph
    void addEdge(int v, int w) {
        adj[v].add(w); // Add w to the list of v.
    } // addEdge

    // prints DFS traversal from a given starting node
    public void DFS(int node) {

        // mark all the vertices as unvisited (false)
        boolean visited[] = new boolean[V];

        // call the recursive helper function to print DFS traversal
        DFSUtil(node, visited);
    } // DFS

    // A function used by DFS
    public void DFSUtil(int node, boolean visited[]) {

        // print the current node and mark it visited
        System.out.print(node + " ");
        visited[node] = true;

        // recursively continue for all unvisited adjacent nodes
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited);
            }
        }
    } // DFSUtil

    public static void main(String args[]) {
        Graph g = new Graph(6);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(2, 3);
        g.addEdge(2, 4);
        g.addEdge(4, 5);
        g.addEdge(1, 3);
        g.addEdge(3, 5);

        System.out.println("Depth First Traversal");

        g.DFS(0);
    } // main
}
