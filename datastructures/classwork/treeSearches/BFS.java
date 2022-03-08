// Class to represent Tree node
class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = null;
        right = null;
    }
}

public class BFS {
    // Root of the Binary Tree
    Node root;

    public BFS() {
        root = null;
    }

    // find the "height" of a tree (the number of nodes along the
    // longest path from the root node down to the farthest leaf node.)
    public int height(Node root) {
        // empty tree has height 0
        if (root == null)
            return 0;
        else {
            // compute height of each subtree
            int lheight = height(root.left);
            int rheight = height(root.right);

            // return the larger of the two heights
            if (lheight > rheight)
                return (lheight + 1);
            else
                return (rheight + 1);
        }
    } // height

    // print level order traversal of tree
    public void printLevelOrder() {
        int h = height(root);
        for (int i = 1; i <= h; i++)
            printCurrentLevel(root, i);
    } // printLevelOrder

    // print nodes at the current level
    public void printCurrentLevel(Node root, int level) {
        if (root == null)
            return;
        // print out the first level
        if (level == 1)
            System.out.print(root.data + " ");
        // recursively print out the following levels
        else if (level > 1) {
            printCurrentLevel(root.left, level - 1);
            printCurrentLevel(root.right, level - 1);
        }
    } // printCurrentLevel

    public static void main(String args[]) {
        BFS tree = new BFS();
        tree.root = new Node(4);
        tree.root.left = new Node(2);
        tree.root.right = new Node(6);
        tree.root.left.left = new Node(1);
        tree.root.left.right = new Node(3);
        tree.root.right.left = new Node(5);
        tree.root.right.right = new Node(7);

        System.out.println("Level order traversal of the binary tree is ");
        tree.printLevelOrder();
    } // main
}
