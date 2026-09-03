# =========================
# Doubly Linked List Implementation in Python
# =========================

# ----------------- Node Class -----------------
class Node:
    def __init__(self, value, next=None, prev=None):
        self.data = value  # Value stored in node
        self.next = next   # Pointer to next node
        self.prev = prev   # Pointer to previous node
        # Time: O(1)
        # Space: O(1)


# ----------------- Doubly Linked List Class -----------------
class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head  # Start of the list
        # Optionally, we can maintain self.tail for O(1) end operations

    # ----------------- Insert at End -----------------
    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:  # Empty list
            self.head = temp
            return

        t = self.head
        while t.next:  # Traverse to last node
            t = t.next
        t.next = temp
        temp.prev = t

        # Time Complexity:
        # Best: O(1) -> list empty
        # Average/Worst: O(n) -> need to traverse n nodes
        # Space Complexity: O(1)

    # ----------------- Insert at Start -----------------
    def insert_at_start(self, value):
        temp = Node(value)
        if self.head is None:  # Empty list
            self.head = temp
            return
        temp.next = self.head  # New node points to old head
        self.head.prev = temp  # Old head points back to new node
        self.head = temp       # Update head

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    # ----------------- Insert After a Given Value -----------------
    def insert_in_middle(self, value, x):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t:
            if t.data == x:
                # Case 1: inserting after last node
                if t.next is None:
                    t.next = temp
                    temp.prev = t
                else:
                    # Case 2: inserting in actual middle
                    temp.next = t.next
                    t.next.prev = temp
                    t.next = temp
                    temp.prev = t
                return
            t = t.next

        print(f"Value {x} not found in the list")

        # Time Complexity:
        # Best: O(1) -> x is at head
        # Average/Worst: O(n) -> traverse n nodes
        # Space Complexity: O(1)

    # ----------------- Delete from Start -----------------
    def delete_from_start(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:  # Only one node
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None  # Disconnect old head

        # Time Complexity: O(1)
        # Space Complexity: O(1)

    # ----------------- Delete from End -----------------
    def delete_from_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:  # Only one node
            self.head = None
            return

        t = self.head
        while t.next.next:  # Traverse to second-last node
            t = t.next
        t.next.prev = None  # Disconnect last node
        t.next = None       # Remove last node

        # Time Complexity:
        # Best: O(1) -> single node
        # Average/Worst: O(n)
        # Space Complexity: O(1)

    # ----------------- Delete a Node by Value -----------------
    def delete_from_middle(self, value):
        """
        Deletes the first node that contains the given value.
        Handles:
        1. Empty list
        2. Node to delete is head
        3. Node to delete is in middle or end
        4. Node not found
        """

        if self.head is None:
            print("Linked List is empty")
            return

        t = self.head

        # Case: Node to delete is head
        if t.data == value:
            self.head = t.next
            if self.head:
                self.head.prev = None
            return

        # Traverse the list to find the node
        while t and t.data != value:
            t = t.next

        # Node not found
        if t is None:
            print(f"Value {value} not found in the list")
            return

        # Node found (middle or last)
        if t.prev:
            t.prev.next = t.next
        if t.next:
            t.next.prev = t.prev

        # Time Complexity:
        # Best: O(1) -> node is head
        # Average/Worst: O(n) -> node is middle or end
        # Space Complexity: O(1)

    # ----------------- Print the List -----------------
    def print_doubly_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        t = self.head
        while t:
            if t.next:
                print(f"{t.data} <=> ", end="")
            else:
                print(f"{t.data} <=> None")
            t = t.next

        # Time Complexity: O(n)
        # Space Complexity: O(1)


# ----------------- Testing the Doubly Linked List -----------------
if __name__ == "__main__":
    obj = DoublyLinkedList()

    # Insert at end
    obj.insert_at_end(10)
    obj.insert_at_end(20)
    obj.insert_at_end(30)
    obj.insert_at_end(40)
    obj.insert_at_end(50)
    obj.print_doubly_linked_list()  # 10 <=> 20 <=> 30 <=> 40 <=> 50 <=> None

    # Insert at start
    obj.insert_at_start(5)
    obj.print_doubly_linked_list()  # 5 <=> 10 <=> 20 <=> 30 <=> 40 <=> 50 <=> None

    # Insert in middle
    obj.insert_in_middle(35, 30)
    obj.print_doubly_linked_list()  # 5 <=> 10 <=> 20 <=> 30 <=> 35 <=> 40 <=> 50 <=> None

    # Delete from start
    obj.delete_from_start()
    obj.print_doubly_linked_list()  # 10 <=> 20 <=> 30 <=> 35 <=> 40 <=> 50 <=> None

    # Delete from end
    obj.delete_from_end()
    obj.print_doubly_linked_list()  # 10 <=> 20 <=> 30 <=> 35 <=> 40 <=> None

    # Delete from middle
    obj.delete_from_middle(30)
    obj.print_doubly_linked_list()  # 10 <=> 20 <=> 35 <=> 40 <=> None

    # Delete a non-existent node
    obj.delete_from_middle(100)     # Value 100 not found in the list