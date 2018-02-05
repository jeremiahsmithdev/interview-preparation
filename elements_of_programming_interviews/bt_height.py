from bt.node import Node

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.right.right = Node("D")

def height(tree):
    if not tree:
        return 0

    return max(height(tree.left) + 1, height(tree.right) + 1)

print(height(root))