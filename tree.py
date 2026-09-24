class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# Create tree
root = Node(10)
root.left = Node(20)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(30)

# Preorder traversal
preorder(root)

