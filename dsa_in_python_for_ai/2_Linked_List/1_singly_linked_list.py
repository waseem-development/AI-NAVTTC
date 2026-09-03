class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next
        # Time: O(1)
        # Space: O(1)


class SinglyLinkedList:
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
        # Best: O(1)   (when list is empty)
        # Avg:  O(n)
        # Worst: O(n)
        # Space: O(1)

        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp

    # Insert at the start
    def insert_at_start(self, value):
        # Time Complexity:
        # Best: O(1)
        # Avg:  O(1)
        # Worst: O(1)
        # Space: O(1)

        temp = Node(value)
        temp.next = self.head
        self.head = temp

    # Insert after a given value x
    def insert_in_middle(self, value, x):
        # Time Complexity:
        # Best: O(1)   (x found at head)
        # Avg:  O(n)
        # Worst: O(n)  (x at end or not found)
        # Space: O(1)

        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        t1 = self.head
        while t1 is not None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next

        print(f"Value {x} not found in the list")

    # -------------------------------
    # Delete Methods
    # -------------------------------

    # Delete from start
    def delete_from_start(self):
        # Time Complexity:
        # Best: O(1)
        # Avg:  O(1)
        # Worst: O(1)
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
        else:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted {deleted_value} from start")

    # Delete from end
    def delete_from_end(self):
        # Time Complexity:
        # Best: O(1)   (only one node)
        # Avg:  O(n)
        # Worst: O(n)
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
            return

        # Only one node
        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            print(f"Deleted {deleted_value} from end")
            return

        # More than one node
        t1 = self.head
        while t1.next.next is not None:
            t1 = t1.next

        deleted_value = t1.next.data
        t1.next = None
        print(f"Deleted {deleted_value} from end")

    # Delete a node by value (middle)
    def delete_from_middle(self, value):
        # Time Complexity:
        # Best: O(1)   (value at head or next node)
        # Avg:  O(n)
        # Worst: O(n)  (value at end or not found)
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
            return

        # If the node to delete is the head
        if self.head.data == value:
            self.delete_from_start()
            return

        t1 = self.head
        while t1.next is not None:
            if t1.next.data == value:
                if t1.next.next is None:
                    print(f"Deleted {value} from last")
                else:
                    print(f"Deleted {value} from middle")

                t1.next = t1.next.next
                return
            t1 = t1.next

        print(f"Value {value} not found in the list")

    # -------------------------------
    # Print Method
    # -------------------------------
    def print_linked_list(self):
        # Time Complexity:
        # Best: O(n)
        # Avg:  O(n)
        # Worst: O(n)
        # Space: O(1)

        if self.head is None:
            print("Linked List is empty")
            return

        t1 = self.head
        while t1 is not None:
            if t1.next is not None:
                print(f"{t1.data} -> ", end="")
            else:
                print(f"{t1.data} -> None")
            t1 = t1.next


# -------------------------------
# Example usage
# -------------------------------
obj = SinglyLinkedList()

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