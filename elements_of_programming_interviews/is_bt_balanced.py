from bt.node import Node

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.right.right = Node("D")

def is_balanced(tree):
    if not tree:
        return 0

    left = is_balanced(tree.left)
    right = is_balanced(tree.right)




print(is_balanced(root))