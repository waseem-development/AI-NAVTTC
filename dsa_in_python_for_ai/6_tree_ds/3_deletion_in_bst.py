# Things to know before Deletion in BST:
# [6, 8, 9, 10, 20, 25, 30, 40, 50]
# n = 25
# In-order Predecessor: 20
# In-order Successor: 30
# if We say that n = 10, so the in-order successor of 10 is 20 so we just have to go one step right and then go as left as possible untill we reach 20 (left most element). And to find in-order predecessor, we need to go one step left and then right most element
# 3 Cases of Deletion of an element: 
# 1- Deletion of Leaf Node: Easier: return None to its parent. -> 
# 2- Deletion of Node having one child: Connect Grand Parent with Child
# 3- Deletion of Node having two childs:

# When coding, we care only about case 2 and case 3, because case 3 will be cared automatically 
# Tree after Inorder Traversing: [6, 8, 9, 10, 20, 25, 30, 32, 40, 50]
# For case 3, deal with its in-order successor or predecessor. Let's say the number is 32 How? Actually replace (copy actually) the number to be deleted with its successor or predecessor. when done we will have duplicated. In our case let's take its in-order successor. The tree becomes like this now;
# [6, 8, 9, 10, 20, 25, 32, 32, 40, 50]. Now when done  we have two 32, but if we see still It is a BST. So now we go to the last node which was our original 32 and delete it
# ----------------- Node Class -----------------
class Node:
    def __init__(self, value):
        self.left = None  
        self.right = None  
        self.data = value  


# ----------------- Insertion -----------------
def insertion_in_bst(root, value):
    if root is None:
        return Node(value)

    elif value == root.data:
        return root

    elif value < root.data:

        root.left = insertion_in_bst(root.left, value)

    else:
        root.right = insertion_in_bst(root.right, value)

    return root


# ----------------- Search -----------------
def search_in_bst(root, value):
    if root is None:
        print(f"Element {value} not found")

    elif value == root.data:
        print(f"Element {value} found")

    elif value < root.data:
        search_in_bst(root.left, value)

    else:
        search_in_bst(root.right, value)


def get_in_order_successor(root):
    """
    Finds the in-order successor of a node in a BST.
    
    Steps:
    1. Go to the right child of the current node.
    2. Then, go as left as possible from there.
       This finds the smallest value that is larger than the current node.
    
    Returns:
        Node object representing the in-order successor
    """
    
    # Step 1: move one step right
    root = root.right
    
    # Step 2: keep going left until we reach the left-most node
    # This is the smallest value in the right subtree → in-order successor
    while root is not None and root.left is not None:
        root = root.left
    
    # Return the found node
    return root

def delete_from_bst(root, value):
    """
    Deletes a node from BST following three main cases:
    1. Leaf node
    2. Node with one child
    3. Node with two children (handled via in-order successor / Predecessor but in our case we have done it using successor)
    """
    if root is None:
        # Value not found
        print(f"Element {value} not found")
        return None

    # Value is smaller → go to left subtree
    elif value < root.data:
        root.left = delete_from_bst(root.left, value)

    # Value is greater → go to right subtree
    elif value > root.data:
        root.right = delete_from_bst(root.right, value)

    # Value matches → this is the node to delete
    else:
        # Case 1 or 2: Node has only one child or no child
        if root.left is None:      # Only right child or leaf
            return root.right
        elif root.right is None:   # Only left child
            return root.left

        # Case 3: Node has two children
        # 1. Find in-order successor
        succ = get_in_order_successor(root)
        # 2. Copy successor's value to current node
        root.data = succ.data
        # 3. Delete the original successor node (it falls into case 1 or 2)
        root.right = delete_from_bst(root.right, succ.data)

    # Return root so parent links stay correct
    return root

def in_order_traversal(root):
    if root is None:
        return []


    return (
        in_order_traversal(root.left)
        + [root.data] 
        + in_order_traversal(root.right)  
    )

root = insertion_in_bst(None, 20)  
root = insertion_in_bst(root, 15)  
root = insertion_in_bst(root, 30)  
root = insertion_in_bst(root, 40)
root = insertion_in_bst(root, 12)
root = insertion_in_bst(root, 18)
root = insertion_in_bst(root, 25)
root = insertion_in_bst(root, 50)

print("In-Order Traversal:", in_order_traversal(root))

delete_from_bst(root, 12)
print("In-Order Traversal:", in_order_traversal(root))

search_in_bst(root, 18)
search_in_bst(root, 100)