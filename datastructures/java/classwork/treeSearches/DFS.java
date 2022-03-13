// Class to represent Tree node
class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = null;
        right = null;
    }
} // node

public class DFS {
    Node root;

    public void printInOrder(Node root) {
        if (root != null) {
            printInOrder(root.left);
            System.out.print(root.data + " ");
            printInOrder(root.right);
        }

    } // printInOrder

    public static void main(String args[]) {
        // create the binary tree
        DFS tree = new DFS();
        tree.root = new Node(4);
        tree.root.left = new Node(2);
        tree.root.right = new Node(6);
        tree.root.left.left = new Node(1);
        tree.root.left.right = new Node(3);
        tree.root.right.left = new Node(5);
        tree.root.right.right = new Node(7);

        tree.printInOrder(tree.root);

    } // main
}
