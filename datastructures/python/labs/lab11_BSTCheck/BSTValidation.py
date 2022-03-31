class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def is_bst(node):
    """true if given binary tree is a binary search tree"""
    return is_bst_util(node, float("-inf"), float("inf"))


def is_bst_util(node, mini, maxi):
    """returns true if the given tree is a bst
    and its values are between the min and max
    """

    # An empty tree is a BST
    if node is None:
        return True

    # false if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # check the subtrees recursively tightening the min/max constraints
    return is_bst_util(node.left, mini, node.data - 1) and is_bst_util(
        node.right, node.data + 1, maxi
    )


if __name__ == "__main__":

    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print(is_bst(root))
