class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# function to do inorder tree traversal
def print_in_order(root):
    if root:
        # recur on left child
        print_in_order(root.left)
        # print the data of node
        print(root.data, end=" ")
        # recur on right child
        print_in_order(root.right)


if __name__ == "__main__":

    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print("Inorder traversal of binary tree is")
    print_in_order(root)
