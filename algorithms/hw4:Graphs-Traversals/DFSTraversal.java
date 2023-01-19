public class DFSTraversal {

    public static int[][] adjMatrix;

    public static void dfs(boolean[] visited, int root, int n) {
        // process current node
        System.out.print(root + " ");

        // mark current node as visited
        visited[root] = true;

        // traverse all adjacent nodes
        for (int i = 0; i < n; i++) {
            // if there is an edge from current node to i
            // and i is not visited then traverse i
            if (adjMatrix[root][i] == 1 && (visited[i] == false)) {
                dfs(visited, i, n);
            }
        }
    } // dfs

    public static void main(String[] args) {
        // number of nodes
        int vtxs = 5;

        // create adjacency matrix
        adjMatrix = new int[vtxs][vtxs];

        // add edges
        adjMatrix[1][0] = 1;
        adjMatrix[1][2] = 1;
        adjMatrix[1][4] = 1;
        adjMatrix[2][0] = 1;
        adjMatrix[3][0] = 1;
        adjMatrix[4][3] = 1;

        // create visited array and initialize it to false
        boolean[] visited = new boolean[5];
        for (int i = 0; i < 5; i++)
            visited[i] = false;

        System.out.print("pre-order DFS starting at node 0: ");
        dfs(visited, 0, vtxs);
        // reset visited array
        for (int i = 0; i < 5; i++)
            visited[i] = false;

        System.out.print("\n\npre-order DFS starting at node 1: ");
        dfs(visited, 1, vtxs);
        // reset visited array
        for (int i = 0; i < 5; i++)
            visited[i] = false;

        System.out.print("\n\npre-order DFS starting at node 2: ");
        dfs(visited, 2, vtxs);
        // reset visited array
        for (int i = 0; i < 5; i++)
            visited[i] = false;

        System.out.print("\n\npre-order DFS starting at node 3: ");
        dfs(visited, 3, vtxs);
        // reset visited array
        for (int i = 0; i < 5; i++)
            visited[i] = false;

        System.out.print("\n\npre-order DFS starting at node 4: ");
        dfs(visited, 4, vtxs);

    } // main
}
