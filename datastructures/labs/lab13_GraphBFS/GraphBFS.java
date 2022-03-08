import java.util.*;

// Class representing a directed graph using adjacency lists
class GraphBFS {
    int V; // Number of Vertices
    LinkedList<Integer>[] adj; // adjacency lists

    // Constructor
    GraphBFS(int V) {
        this.V = V;
        adj = new LinkedList[V];

        for (int i = 0; i < adj.length; i++)
            adj[i] = new LinkedList<Integer>();
    }

    // To add an edge to graph
    void addEdge(int v, int w) {
        adj[v].add(w); // Add w to the list of v.
    } // addEdge

    // prints BFS traversal from a given starting node
    public void BFS(int node) {

        // mark all the vertices as unvisited (false)
        boolean visited[] = new boolean[V];

        // create a queue for BFS
        LinkedList<Integer> queue = new LinkedList<Integer>();

        // print the current node and mark it visited
        queue.add(node);
        visited[node] = true;

        while (queue.size() != 0) {
            // dequeue a vertex from queue and print it
            node = queue.poll();
            System.out.print(node + " ");

            // if an adjacent node is hasnt been visited,
            // enqueue it and mark it visited
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    queue.add(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
    } // BFS

    public static void main(String args[]) {
        GraphBFS g = new GraphBFS(6);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(2, 3);
        g.addEdge(2, 4);
        g.addEdge(4, 5);
        g.addEdge(1, 3);
        g.addEdge(3, 5);

        System.out.println("Breadth First Traversal");

        g.BFS(0);
    } // main
}
