from bt.node import Node

root = Node(1)
root.left = Node(3)
root.left.right = Node(4)
root.left.left = Node(3)

def root_to_leaf_sum(tree, temp_sum, target_sum):
    if tree is None:
        return False

    temp_sum += tree.data
    if tree.left is None and tree.right is None:
        return temp_sum == target_sum

    return root_to_leaf_sum(tree.left, temp_sum, target_sum) or root_to_leaf_sum(tree.right, temp_sum, target_sum)

print(root_to_leaf_sum(root, 0, 7))