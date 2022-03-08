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

public class BinaryTree {

    Node root = null;

    // print the in order traversal of the tree
    public void inOrder(Node root) {
        if (root != null) {
            inOrder(root.left);
            System.out.print(root.data + " ");
            inOrder(root.right);
        }
    } // inOrder

    public Node deleteNode(Node root, int data) {
        if (root == null) {
            return root;
        }
        // if the number to delete is less than the current node, go left
        if (data < root.data) {
            root.left = deleteNode(root.left, data);
        }
        // if the number to delete is greater than the current node, go right
        else if (data > root.data) {
            root.right = deleteNode(root.right, data);
        }
        // if the number to delete is the current node
        else {
            // if either the left or right child is null, return that node
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }
            // replace the root with the leftmost leaf of the right tree
            root.data = leftmostLeaf(root.right);
            // delete the duplicate leaf node
            root.right = deleteNode(root.right, root.data);
        }
        return root;
    } // deleteNode

    // find the leftmost leaf of the tree
    public int leftmostLeaf(Node root) {
        int value = root.data;
        // keep going down the left children of the until a leaf is reached
        while (root.left != null) {
            value = root.left.data;
            root = root.left;
        }
        // return the value held by the leaf
        return value;
    } // leftmostLeaf

    public static void main(String[] args) {

        BinaryTree tree = new BinaryTree();
        tree.root = new Node(4);
        tree.root.left = new Node(2);
        tree.root.right = new Node(6);
        tree.root.left.left = new Node(1);
        tree.root.left.right = new Node(3);
        tree.root.right.left = new Node(5);
        tree.root.right.right = new Node(7);

        // print tree before deletion
        System.out.print("Tree before root deletion: ");
        tree.inOrder(tree.root);
        System.out.println();

        // delete root node and print tree again
        tree.deleteNode(tree.root, tree.root.data);
        System.out.print("Tree after root deletion: ");
        tree.inOrder(tree.root);

    } // main
}
