class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self._insert(root.left, value)
        elif value > root.data:
            root.right = self._insert(root.right, value)
        return root

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None or root.data == value:
            return root
        if value < root.data:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)

    def findMinimum(self, root):
        while root.left is not None:
            root = root.left
        return root

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return root
        if value < root.data:
            root.left = self._delete(root.left, value)
        elif value > root.data:
            root.right = self._delete(root.right, value)
        else:
            # Case 1 — no children
            if root.left is None and root.right is None:
                return None
            # Case 2 — one child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 3 — two children
            else:
                temp = self.findMinimum(root.right)
                root.data = temp.data
                root.right = self._delete(root.right, temp.data)
        return root

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        print("Inorder:  ", result)

    def _inorder(self, root, result):
        if root is None:
            return
        self._inorder(root.left, result)
        result.append(root.data)
        self._inorder(root.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        print("Preorder: ", result)

    def _preorder(self, root, result):
        if root is None:
            return
        result.append(root.data)
        self._preorder(root.left, result)
        self._preorder(root.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        print("Postorder:", result)

    def _postorder(self, root, result):
        if root is None:
            return
        self._postorder(root.left, result)
        self._postorder(root.right, result)
        result.append(root.data)

if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    bst.inorder()
    bst.preorder()
    bst.postorder()

    found = bst.search(40)
    print(f"Search 40: {'Found' if found else 'Not Found'}")

    bst.delete(30)
    print("After deleting 30: ", end="")
    bst.inorder()