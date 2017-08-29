class Node():
    def __init__(self, key = None, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def no_children(self):
        return (self.left != None) + (self.right != None)

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        parent = None
        current = self.root
        new_node = Node(key=key)
        while current != None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if parent == None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
            new_node.parent = parent
        else:
            parent.right = new_node
            new_node.parent = parent

    def search(self, key):
        current = self.root
        while current != None and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if current != None:
            return True
        return False

    def get_min(self):
        parent = None
        current = self.root
        while current != None:
            parent = current
            current = current.left
        return parent.key

    def get_max(self):
        parent = None
        current = self.root
        while current != None:
            parent = current
            current = current.right
        return parent.key

    def dfs(self, recursive = True):
        if recursive:
            self._dfs(self.root)
        else:
            self._dfs_iterative(self.root)

    #yes -- same as preorder
    def _dfs(self, node):
        if node == None or node.key == None:
            return
        print(node.key)
        self._dfs(node.left)
        self._dfs(node.right)

    def _dfs_iterative(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            head = stack.pop()
            if head.right != None and head.right.key != None:
                stack.append(head.right)
            if head.left != None and head.left.key != None:
                stack.append(head.left)
            print(head.key)

    def bfs(self):
        self._bst(self.root)

    def delete(self, key):
        return self._delete(key, self.root)

    def _delete(self, key, node):
        current = node
        while current != None and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if current == None:
            return False
        #if no children, simply remove
        if current.no_children() == 0: #
            if current.parent.key > current.key:
                current.parent.left = None
            else:
                current.parent.right = None
        elif current.no_children() == 1:
            if current.parent.key > current.key:
                if current.left != None:
                    current.parent.left = current.left
                else:
                    current.parent.left = current.right
            else:
                if current.left != None:
                    current.parent.right = current.left
                else:
                    current.parent.right = current.right
        else: #two children
            #1: find min node in right subtree
            right_min = None
            right_root = current.right
            while right_root != None:
                right_min = right_root
                right_root = right_root.left
            #2: replace current node's key with min of right subtree
            current.key = right_min.key
            #3: remove key again
            self._delete(right_min.key, current.right)

        return True

    #only doing iterative
    def _bst(self, node):
        queue = []
        queue.append(node)
        while len(queue) > 0:
            head = queue.pop(0)
            if head.left != None and head.left.key != None:
                queue.append(head.left)
            if head.right != None and head.right.key != None:
                queue.append(head.right)
            print(head.key)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node == None or node.key == None:
            return
        self._inorder(node.left)
        print(node.key)
        self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node == None:
            return
        print(node.key)
        self._preorder(node.left)
        self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node == None or node.key == None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.key)

bst = BinarySearchTree()
bst.insert(6)
bst.insert(5)
bst.insert(2)
bst.insert(5)
bst.insert(7)
bst.insert(8)

bst.inorder()
print()
bst.preorder()
print()
bst.postorder()
print()
print(bst.search(10))
print()
bst.dfs()
print()
bst.dfs(recursive=False)
print()
bst.bfs()

print(bst.get_min())

#bst.delete(8)
#bst.delete(7)
#bst.delete(5)
print()

bst.bfs()

#bst.delete(6)

print()

bst.bfs()

def is_bst(root):
    if root == None:
        return True
    is_current_bst = True
    if root.left != None and root.left.key >= root.key:
        is_current_bst = False
    if root.right != None and root.right.key < root.key:
        is_current_bst = False
    return is_current_bst and is_bst(root.left) and is_bst(root.right)

print()

print(is_bst(bst.root))

bst.root.key = 8

print(is_bst(bst.root))
