# A Binary Tree with one extra rule: the LEFT subtree always contains values SMALLER than the parent, and the RIGHT subtree always contains values LARGER. This rule makes searching incredibly fast — O(log n) instead of O(n)!
# Even its name suggests that a tree that reduces search time
# time complexity in Simple Binary Tree = O(n)
# time complexity in Binary Search Tree = O(log(n)) ==> faster
# Numper of itertaions = height of the tree and height of tree = log(n)
# Interview Questions:
# Q-1: Print all the elements of a BST in increasing order
# Q-2: How to check a valid binary seach tree
# Q-3: Inorder-Traversal of BST
# But!!!!! All of these questions are same!!! so the interviewe confuses you

# =========================
# Binary Search Tree (BST)
# =========================

# A BST follows this rule:
# Left subtree → values smaller than parent
# Right subtree → values greater than parent
# This allows faster search: O(log n) (if balanced)


# ----------------- Node Class -----------------
class Node:
    def __init__(self, value):
        # Each node stores:
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.data = value  # actual value of the node


# ----------------- Insertion -----------------
def insertion_in_bst(root, value):
    # Base case:
    # If we reach an empty spot → insert new node here
    if root is None:
        return Node(value)

    # If value already exists → do nothing (avoid duplicates)
    elif value == root.data:
        return root # Each subtree says "I updated my subtree → now I return myself upward"

    # If value is smaller → go to LEFT subtree
    elif value < root.data:
        # Recursively insert into left subtree
        # and re-attach the updated subtree back to root.left
        root.left = insertion_in_bst(root.left, value)

    # If value is greater → go to RIGHT subtree
    else:
        # Same logic for right side
        root.right = insertion_in_bst(root.right, value)

    # IMPORTANT:
    # Return the root so parent nodes can reconnect properly
    return root


# ----------------- Search -----------------
def search_in_bst(root, value):
    # If we reach NULL → value does not exist
    if root is None:
        print(f"Element {value} not found")

    # If value matches current node → found
    elif value == root.data:
        print(f"Element {value} found")

    # If value is smaller → search in LEFT subtree
    elif value < root.data:
        search_in_bst(root.left, value)

    # If value is greater → search in RIGHT subtree
    else:
        search_in_bst(root.right, value)


# ----------------- In-order Traversal -----------------
def inorder_traversal(root):
    # Base case: empty tree → return empty list
    if root is None:
        return []

    # In-order traversal:
    # Left → Root → Right
    # For BST, this always gives SORTED order
    return (
        inorder_traversal(root.left)  # all smaller values
        + [root.data]  # current node
        + inorder_traversal(root.right)  # all larger values
    )


# ----------------- Build Tree -----------------

# Instead of manually linking nodes,
# we insert values one by one using BST logic

# ----------------- Build BST using insertion -----------------

# Start with an empty tree
# First insertion: tree is empty, so the new node becomes the root
root = insertion_in_bst(None, 20)  # root now points to Node(20)

# Insert 15
# Since 15 < 20, it goes to the left subtree of root
# root.left is updated inside the function
root = insertion_in_bst(root, 15)  # root still Node(20), left child updated

# Insert 30
# 30 > 20, goes to the right subtree
# root.right is updated recursively
root = insertion_in_bst(root, 30)  # root still Node(20), right child updated

# Insert 12
# 12 < 20 → go left to Node(15)
# 12 < 15 → go left of Node(15)
# Node(15).left is updated to Node(12)
root = insertion_in_bst(root, 12)

# Insert 18
# 18 < 20 → left subtree
# 18 > 15 → right subtree of Node(15)
# Node(15).right updated to Node(18)
root = insertion_in_bst(root, 18)

# Insert 40
# 40 > 20 → right subtree
# 40 > 30 → right subtree of Node(30)
# Node(30).right updated to Node(40)
root = insertion_in_bst(root, 40)

# ----------------- Resulting BST -----------------
#           20
#         /    \
#       15      30
#      /  \       \
#    12    18      40

# Note:
# - Even though root rarely changes after the first insertion,
#   we always assign root = insertion_in_bst(...) for safety
# - Recursive calls always return the updated subtree
# - This pattern is crucial for deletion and other BST operations

# Final Tree Structure:
#         20
#        /  \
#      15    30
#     / \      \
#   12  18      40

# ----------------- Output -----------------

# In-order traversal prints values in sorted order
print("In-Order Traversal:", inorder_traversal(root))
# Output: [12, 15, 18, 20, 30, 40]

# Search examples
search_in_bst(root, 18)  # Found
search_in_bst(root, 100)  # Not Found
