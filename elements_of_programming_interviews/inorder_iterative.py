from bt.node import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

def inorder(tree):
    temp = [] # implement this as deque...lazy for now
    result = []

    node = tree

    while temp or node is not None:
        if node:
            temp.insert(0,node)
            node = node.left
        else:
            node = temp.pop(0)
            result.append(node.data)
            node = node.right

    return result

print(inorder(root))