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

public class BinaryTree {
    Node root;

    // true if given search tree is binary search tree
    public boolean isBST() {
        return isBSTUtil(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    } // isBST

    // returns true if the given tree is a bst
    // and its values are between the min and max
    public boolean isBSTUtil(Node node, int min, int max) {
        // an empty tree is BST
        if (node == null)
            return true;

        // false if this node violates the min/max constraints
        if (node.data <= min || node.data >= max)
            return false;

        // check the subtrees recursively tightening the min/max constraints
        return (isBSTUtil(node.left, min, node.data) && isBSTUtil(node.right, node.data, max));
    } // isBSTUtil

    public static void main(String args[]) {
        // create the binary tree
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(4);
        tree.root.left = new Node(2);
        tree.root.right = new Node(6);
        tree.root.left.left = new Node(1);
        tree.root.left.right = new Node(3);
        tree.root.right.left = new Node(5);
        tree.root.right.right = new Node(7);

        // prints true or false depending on whether the tree is a BST
        System.out.println(tree.isBST());
    } // main
}
