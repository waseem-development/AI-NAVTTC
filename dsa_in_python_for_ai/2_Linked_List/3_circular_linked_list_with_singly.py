class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next
        # Time: O(1)
        # Space: O(1)


class CircularSinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        # Time: O(1)
        # Space: O(1)

    # -------------------------------
    # Insert Methods
    # -------------------------------

    # Insert at the end
    def insert_at_end(self, value):
        # Time Complexity:
        # Best:  O(1) - list is empty, just set head
        # Avg:   O(n) - traverse to find last node
        # Worst: O(n) - traverse entire list to last node
        # Space: O(1) - only one new node created

        temp = Node(value)
        if self.head is None:
            # Empty list: node points to itself
            self.head = temp
            temp.next = self.head
        else:
            t1 = self.head
            # Traverse until we reach the last node (points back to head)
            while t1.next is not self.head:
                t1 = t1.next
            t1.next = temp
            temp.next = self.head  # new last node points back to head

    # Insert at the start
    def insert_at_start(self, value):
        # Time Complexity:
        # Best:  O(1) - list is empty
        # Avg:   O(n) - must find last node to update its next pointer
        # Worst: O(n) - traverse entire list to find last node
        # Space: O(1) - only one new node created

        temp = Node(value)
        if self.head is None:
            # Empty list: node points to itself
            self.head = temp
            temp.next = self.head
        else:
            t1 = self.head
            # Find last node so we can update it to point to new head
            while t1.next is not self.head:
                t1 = t1.next
            temp.next = self.head   # new node points to old head
            self.head = temp        # update head to new node
            t1.next = self.head     # last node points to new head

    # Insert after a given value x
    def insert_in_middle(self, value, x):
        # Time Complexity:
        # Best:  O(1) - x found at head
        # Avg:   O(n) - x found somewhere in the middle
        # Worst: O(n) - x at last node or not found
        # Space: O(1) - only one new node created

        temp = Node(value)
        if self.head is None:
            # Empty list: node points to itself
            self.head = temp
            temp.next = self.head
            return

        t1 = self.head
        while True:
            if t1.data == x:
                # Found x: insert new node after it
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
            if t1 is self.head:  # completed full circle, x not found
                break

        print(f"Value {x} not found in the list")

    # -------------------------------
    # Delete Methods
    # -------------------------------

    # Delete from start
    def delete_from_start(self):
        # Time Complexity:
        # Best:  O(1) - empty list or single node
        # Avg:   O(n) - must find last node to update its next pointer
        # Worst: O(n) - traverse entire list to find last node
        # Space: O(1) - no extra space used

        if self.head is None:
            print("Linked List is empty")
            return

        deleted_value = self.head.data
        if self.head.next is self.head:
            # Only one node: just remove it
            self.head = None
        else:
            t1 = self.head
            # Find last node so we can update it to point to new head
            while t1.next is not self.head:
                t1 = t1.next
            self.head = self.head.next  # move head forward
            t1.next = self.head         # last node points to new head
        print(f"Deleted {deleted_value} from start")

    # Delete from end
    def delete_from_end(self):
        # Time Complexity:
        # Best:  O(1) - only one node in list
        # Avg:   O(n) - traverse to second-last node
        # Worst: O(n) - traverse entire list to second-last node
        # Space: O(1) - no extra space used

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is self.head:
            # Only one node: just remove it
            deleted_value = self.head.data
            self.head = None
            print(f"Deleted {deleted_value} from end")
            return

        t1 = self.head
        # Stop at second-last node (its next.next is head)
        while t1.next.next is not self.head:
            t1 = t1.next
        deleted_value = t1.next.data
        t1.next = self.head  # second-last node now points to head
        print(f"Deleted {deleted_value} from end")

    # Delete a node by value
    def delete_from_middle(self, value):
        # Time Complexity:
        # Best:  O(1) - value is at head
        # Avg:   O(n) - value found somewhere in middle
        # Worst: O(n) - value at last node or not found
        # Space: O(1) - no extra space used

        if self.head is None:
            print("Linked List is empty")
            return

        # If the node to delete is the head
        if self.head.data == value:
            self.delete_from_start()
            return

        t1 = self.head
        # Traverse until we complete the circle
        while t1.next is not self.head:
            if t1.next.data == value:
                if t1.next.next is self.head:
                    print(f"Deleted {value} from last")
                else:
                    print(f"Deleted {value} from middle")
                t1.next = t1.next.next  # skip over the deleted node
                return
            t1 = t1.next

        print(f"Value {value} not found in the list")

    # -------------------------------
    # Print Method
    # -------------------------------

    def print_linked_list(self):
        # Time Complexity:
        # Best:  O(n) - always traverses entire list
        # Avg:   O(n)
        # Worst: O(n)
        # Space: O(1) - no extra space used

        if self.head is None:
            print("Linked List is empty")
            return

        t1 = self.head
        while True:
            if t1.next is not self.head:
                print(f"{t1.data} -> ", end="")
            else:
                # Last node: show it loops back to head
                print(f"{t1.data} -> (back to head: {self.head.data})")
            t1 = t1.next
            if t1 is self.head:  # completed full circle, stop
                break


# -------------------------------
# Example usage
# -------------------------------
obj = CircularSinglyLinkedList()

obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.print_linked_list()

obj.insert_at_start(5)
obj.print_linked_list()

obj.insert_in_middle(25, 20)
obj.print_linked_list()

obj.delete_from_start()
obj.print_linked_list()

obj.delete_from_end()
obj.print_linked_list()

obj.delete_from_middle(20)
obj.print_linked_list()

obj.delete_from_middle(25)
obj.print_linked_list()

obj.delete_from_middle(10)
obj.print_linked_list()

obj.delete_from_end()
obj.delete_from_middle(10)