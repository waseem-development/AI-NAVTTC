# Why to specify Traversal specifically for Tree? Beasue tree has different ways to traverse:
# 1 ((left: 2) (right: 3)):
# | 1 2 3 | 1 3 2 | 2 1 3 |
# | 2 3 1 | 3 1 2 | 3 2 1 |
# Do we have to print it all 6 ways? No we first print root then go left to right:
# So for focusing on root we divide these ways in 3 ways: 
# 1) Category 1: Root is in the beginning | 1 2 3 | 1 3 2 | 
# 2) Category 2: Root is in the middle | 2 1 3 | | 3 1 2 |
# 3) Category 3: Root is in the end | 2 3 1 | | 3 2 1 |
# So out of these 6 we eleminate 3 of them and select only 1 from each categoty and 3 possibilities left
# 1- Pre-order Traversal: Root -> Left -> Right
# 2- In-order Traversal:  Left -> Root -> Right
# 3- Post-order Traversal: Left -> Right -> Root 

# ----------------- Node Class -----------------
class Node: 
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


# ----------------- Traversals -----------------

def pre_order_traversal(root):
    if root is None:
        return []
    
    return (
        [root.data] +
        pre_order_traversal(root.left) +
        pre_order_traversal(root.right)
    )


def inorder_traversal(root):
    if root is None:
        return []
    
    return (
        inorder_traversal(root.left) +
        [root.data] +
        inorder_traversal(root.right)
    )


def post_order_traversal(root):
    if root is None:
        return []
    
    return (
        post_order_traversal(root.left) +
        post_order_traversal(root.right) +
        [root.data]
    )


# ----------------- Build Tree -----------------

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)


# ----------------- Print Results -----------------

print("Pre-Order Traversal:", pre_order_traversal(root))
print("In-Order Traversal:", inorder_traversal(root))
print("Post-Order Traversal:", post_order_traversal(root))