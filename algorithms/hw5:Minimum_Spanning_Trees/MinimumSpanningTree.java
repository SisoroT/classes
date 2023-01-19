public class MinimumSpanningTree {
    // define the count of vertices available in the graph
    private static final int countOfVertices = 9;

    // finds the vertex v that has minimum
    // the key-value and that is not added MST yet
    int findMinKeyVertex(int keys[], Boolean mstSet[]) {
        // initialize min value and its index
        int minimum_index = -1;
        int minimum_value = Integer.MAX_VALUE;

        // iterate over all vertices to find minimum key-value vertex
        for (int vertex = 0; vertex < countOfVertices; vertex++)
            if (mstSet[vertex] == false && keys[vertex] < minimum_value) {
                minimum_value = keys[vertex];
                minimum_index = vertex;
            }
        return minimum_index;
    } // findMinKeyVertex

    // print the constructed MST stored in mstArray[]
    void showMinimumSpanningTree(int mstArray[], int graphArray[][]) {
        System.out.println("Edge \t\t Weight");
        for (int j = 1; j < countOfVertices; j++)
            System.out.println(mstArray[j] + " <-> " + j + "\t \t" + graphArray[j][mstArray[j]]);
    } // showMinimumSpanningTree

    // construct and print the MST
    void designMST(int graphArray[][]) {
        int mstArray[] = new int[countOfVertices];
        // array for selecting edge having minimum weight in cut
        int keys[] = new int[countOfVertices];

        // array for representing the set of vertices in MST
        Boolean mstSet[] = new Boolean[countOfVertices];

        // set the value of the keys to infinity
        for (int j = 0; j < countOfVertices; j++) {
            keys[j] = Integer.MAX_VALUE;
            mstSet[j] = false;
        }

        // set value 0 to the 1st vertex because first vertices always include in MST
        keys[0] = 0;
        mstArray[0] = -1;

        // the vertices in the MST will be equal to the countOfVertices
        for (int i = 0; i < countOfVertices - 1; i++) {
            // select the vertex with minimum key that is not yet
            // added in the MST yet from the set of vertices
            int edge = findMinKeyVertex(keys, mstSet);
            // add selected minimum key vertex to the mstSet
            mstSet[edge] = true;

            // change key value and parent index of all adjacent vertices of selected vertex
            // only the vertices that aren't included in the mst are considered
            for (int vertex = 0; vertex < countOfVertices; vertex++)

                // update key when the value of graphArray[edge][vertex]
                // is smaller than key[vertex]
                if (graphArray[edge][vertex] != 0 && mstSet[vertex] == false
                        && graphArray[edge][vertex] < keys[vertex]) {
                    mstArray[vertex] = edge;
                    keys[vertex] = graphArray[edge][vertex];
                }
        }

        // print the constructed Minimum Spanning Tree
        showMinimumSpanningTree(mstArray, graphArray);
    } // designMST

    public static void main(String[] args) {
        MinimumSpanningTree mst = new MinimumSpanningTree();

        // adjacency matrix that defines the graph for MST.
        int graphArray[][] = new int[][] { { 0, 4, 0, 0, 0, 0, 0, 8, 0 }, { 4, 0, 8, 0, 0, 0, 0, 11, 0 },
                { 0, 8, 0, 7, 0, 4, 0, 0, 2 }, { 0, 0, 7, 0, 9, 14, 0, 0, 0 }, { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
                { 0, 0, 4, 14, 10, 0, 2, 0, 0 }, { 0, 0, 0, 0, 0, 2, 0, 1, 6 }, { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
                { 0, 0, 2, 0, 0, 0, 6, 7, 0 } };

        // Print the Minimum Spanning Tree solution
        mst.designMST(graphArray);
    } // main
}
