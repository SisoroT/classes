class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def print_in_order(root):
    """Prints the in order traversal of tree."""
    if root:
        # recur on left child
        print_in_order(root.left)
        # print the data of node
        print(root.data, end=" ")
        # recur on right child
        print_in_order(root.right)


def leftmost_leaf(node: Node) -> int:
    """Find the leftmost leaf of the tree."""
    curr = node

    # loop down to find the leftmost leaf
    while curr.left is not None:
        curr = curr.left

    # return data of the leftmost leaf node
    return curr.data


def delete_node(root, data: int) -> Node:
    """Given a binary search tree and data to delete, this function
    deletes the data and returns the new root.
    """
    # base case
    if root is None:
        return root

    # if the data to be deleted is smaller than
    # the root's data then it lies in left subtree
    if data < root.data:
        root.left = delete_node(root.left, data)

    # if the data to be deleted is greater than
    # the root's data then it lies in right subtree
    elif data > root.data:
        root.right = delete_node(root.right, data)

    # if data is same as root's data, then this is the node to be deleted
    else:
        # if either the left or right child is null, return that node
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # replace the root with the leftmost leaf of the right tree
        root.data = leftmost_leaf(root.right)

        # delete the duplicate leaf node
        root.right = delete_node(root.right, root.data)

    return root


if __name__ == "__main__":

    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    # print tree before deletion
    print("Tree before root deletion: ")
    print_in_order(root)
    print("\n")

    # delete root node and print tree again
    delete_node(root, root.data)
    print("Tree after root deletion: ")
    print_in_order(root)
