# =========================
# Circular Doubly Linked List Implementation in Python
# =========================
#
# ----------------- Node Class -----------------
class Node:
    def __init__(self, value, next=None, prev=None):
        self.data = value  # Value stored in node
        self.next = next   # Pointer to next node
        self.prev = prev   # Pointer to previous node
        # Time: O(1)
        # Space: O(1)


# ----------------- Circular Doubly Linked List Class -----------------
class CircularDoublyLinkedList:
    def __init__(self, head=None):
        self.head = head  # Start of the list

    # ----------------- Insert at End -----------------
    def insert_at_end(self, value):
        # Time Complexity:
        # Best:  O(1) -> list is empty
        # Avg:   O(n) -> traverse to last node
        # Worst: O(n) -> traverse entire list
        # Space: O(1)

        temp = Node(value)
        if self.head is None:
            # Single node points to itself in both directions
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
            return

        t = self.head
        while t.next is not self.head:  # traverse to last node
            t = t.next
        t.next = temp         # last node points to new node
        temp.prev = t         # new node points back to old last
        temp.next = self.head # new node wraps to head
        self.head.prev = temp # head points back to new last node

    # ----------------- Insert at Start -----------------
    def insert_at_start(self, value):
        # Time Complexity:
        # Best:  O(1) -> list is empty
        # Avg:   O(n) -> must find last node to update its next/prev
        # Worst: O(n) -> traverse entire list to find last node
        # Space: O(1)

        temp = Node(value)
        if self.head is None:
            # Single node points to itself in both directions
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
            return

        t = self.head
        while t.next is not self.head:  # find last node
            t = t.next
        temp.next = self.head  # new node points to old head
        self.head.prev = temp  # old head points back to new node
        t.next = temp          # last node points to new head
        temp.prev = t          # new node points back to last node
        self.head = temp       # update head

    # ----------------- Insert After a Given Value -----------------
    def insert_in_middle(self, value, x):
        # Time Complexity:
        # Best:  O(1) -> x is at head
        # Avg:   O(n) -> traverse to find x
        # Worst: O(n) -> x at last node or not found
        # Space: O(1)

        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
            return

        t = self.head
        while True:
            if t.data == x:
                temp.next = t.next    # new node points to next
                temp.prev = t         # new node points back to t
                t.next.prev = temp    # next node points back to new node
                t.next = temp         # t points to new node
                # if inserted after last node, update head.prev
                if temp.next is self.head:
                    self.head.prev = temp
                return
            t = t.next
            if t is self.head:  # completed full circle, x not found
                break

        print(f"Value {x} not found in the list")

    # ----------------- Delete from Start -----------------
    def delete_from_start(self):
        # Time Complexity:
        # Best:  O(1) -> empty or single node
        # Avg:   O(n) -> must find last node to update pointers
        # Worst: O(n) -> traverse entire list to find last node
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is self.head:  # only one node
            self.head = None
            return

        t = self.head
        while t.next is not self.head:  # find last node
            t = t.next
        self.head = self.head.next  # move head forward
        self.head.prev = t          # new head points back to last node
        t.next = self.head          # last node points to new head

    # ----------------- Delete from End -----------------
    def delete_from_end(self):
        # Time Complexity:
        # Best:  O(1) -> empty or single node
        # Avg:   O(n) -> traverse to second-last node
        # Worst: O(n) -> traverse entire list
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is self.head:  # only one node
            self.head = None
            return

        t = self.head
        while t.next.next is not self.head:  # find second-last node
            t = t.next
        t.next = self.head   # second-last now points to head
        self.head.prev = t   # head points back to new last node

    # ----------------- Delete a Node by Value -----------------
    def delete_from_middle(self, value):
        # Time Complexity:
        # Best:  O(1) -> value is at head
        # Avg:   O(n) -> value in middle
        # Worst: O(n) -> value at last node or not found
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
            return

        # Case: node to delete is head
        if self.head.data == value:
            self.delete_from_start()
            return

        t = self.head.next
        while t is not self.head:
            if t.data == value:
                t.prev.next = t.next  # skip over deleted node (forward)
                t.next.prev = t.prev  # skip over deleted node (backward)
                return
            t = t.next

        print(f"Value {value} not found in the list")

    # ----------------- Print the List -----------------
    def print_linked_list(self):
        # Time Complexity:
        # Best:  O(n)
        # Avg:   O(n)
        # Worst: O(n)
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
            return

        t = self.head
        while True:
            if t.next is not self.head:
                print(f"{t.data} <=> ", end="")
            else:
                # Last node: show it loops back to head
                print(f"{t.data} <=> (back to head: {self.head.data})")
            t = t.next
            if t is self.head:  # completed full circle, stop
                break


# ----------------- Testing the Circular Doubly Linked List -----------------
if __name__ == "__main__":
    obj = CircularDoublyLinkedList()

    # Insert at end
    obj.insert_at_end(10)
    obj.insert_at_end(20)
    obj.insert_at_end(30)
    obj.insert_at_end(40)
    obj.insert_at_end(50)
    obj.print_linked_list()  # 10 <=> 20 <=> 30 <=> 40 <=> 50 <=> (back to head: 10)

    # Insert at start
    obj.insert_at_start(5)
    obj.print_linked_list()  # 5 <=> 10 <=> 20 <=> 30 <=> 40 <=> 50 <=> (back to head: 5)

    # Insert in middle
    obj.insert_in_middle(35, 30)
    obj.print_linked_list()  # 5 <=> 10 <=> 20 <=> 30 <=> 35 <=> 40 <=> 50 <=> (back to head: 5)

    # Delete from start
    obj.delete_from_start()
    obj.print_linked_list()  # 10 <=> 20 <=> 30 <=> 35 <=> 40 <=> 50 <=> (back to head: 10)

    # Delete from end
    obj.delete_from_end()
    obj.print_linked_list()  # 10 <=> 20 <=> 30 <=> 35 <=> 40 <=> (back to head: 10)

    # Delete from middle
    obj.delete_from_middle(30)
    obj.print_linked_list()  # 10 <=> 20 <=> 35 <=> 40 <=> (back to head: 10)

    # Delete a non-existent node
    obj.delete_from_middle(100)  # Value 100 not found in the list