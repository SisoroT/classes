class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def height(node):
    """find the "height" of a tree (the number of nodes along the
    longest path from the root node down to the farthest leaf node.)
    """
    # empty tree has height 0
    if node is None:
        return 0
    else:
        # compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # return the larger of the two heights
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# print nodes at a current level
def print_current_level(root, level):
    if root is None:
        return
    # print out the first level
    if level == 1:
        print(root.data, end=" ")
    # recursively print out the following levels
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)


# print level order traversal of tree
def print_level_order(root):
    h = height(root)
    for i in range(1, h + 1):
        print_current_level(root, i)


if __name__ == "__main__":

    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print("Level order traversal of the binary tree is")
    print_level_order(root)
